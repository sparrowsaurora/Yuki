import whisper
import sounddevice as sd
import numpy as np
import queue
import time
import os

class Speech_to_text:
    def __init__(self):
        self.model = whisper.load_model("base")
        self.SAMPLE_RATE = 16000
        self.CHUNK_SIZE = int(self.SAMPLE_RATE * 0.5)  # 500ms per chunk

        self.audio_queue = queue.Queue()
        self.SILENCE_THRESHOLD = self.calibrate_noise_floor()

        self.LISTEN_TIMEOUT = 2.0  # Stop listening after X seconds of silence
        self.MIN_SPEECH_DURATION = 1.0  # Must speak at least X seconds to be valid
        
        self.transcription_file = "input_control/stt_output.txt"

    def calibrate_noise_floor(self, duration=2):
        print("Calibrating background noise... Stay silent.")
        noise_samples = []
        def callback(indata, frames, time, status):
            noise_samples.append(indata.copy())

        with sd.InputStream(samplerate=self.SAMPLE_RATE, channels=1, callback=callback):
            time.sleep(duration)

        noise_samples = np.concatenate(noise_samples, axis=0)
        noise_energy = np.linalg.norm(noise_samples) / len(noise_samples)
        threshold = noise_energy * 2  # Adjust multiplier based on sensitivity

        print(f"Noise floor: {noise_energy:.5f}, Threshold set to: {threshold:.5f}")
        return threshold

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(f"Audio error: {status}")
        self.audio_queue.put(indata.copy())

    def is_silent(self, audio_data):
        energy = np.linalg.norm(audio_data) / len(audio_data)
        return energy < self.SILENCE_THRESHOLD

    def process_audio(self):
        speech_segments = []
        last_speech_time = time.time()

        while True:
            audio_data = self.audio_queue.get()
            audio_data = audio_data.mean(axis=1).astype(np.float32)

            if not self.is_silent(audio_data):
                speech_segments.append(audio_data)
                last_speech_time = time.time()  # Reset silence timer
            elif time.time() - last_speech_time > self.LISTEN_TIMEOUT:
                break  # Stop if silence is detected for too long

        if len(speech_segments) < self.MIN_SPEECH_DURATION * (self.SAMPLE_RATE // len(audio_data)):
            print("Speech too short, ignoring input.")
            return None  # Ignore very short noises

        full_audio = np.concatenate(speech_segments, axis=0)
        result = self.model.transcribe(full_audio, fp16=False)

        if not result['text'].strip():
            print("No speech detected.")
            return None

        return result['text'].strip()

    def get_speech(self):
        with sd.InputStream(
            samplerate=self.SAMPLE_RATE,
            channels=1,
            callback=self.audio_callback,
            blocksize=self.CHUNK_SIZE
        ):
            print("Listening... Speak to activate.")
            transcription = self.process_audio()

            if transcription:
                self.save_transcription(transcription)
                return transcription
            return None

    def save_transcription(self, text):
        with open(self.transcription_file, "a") as f:
            f.write(text + "\n")

    def get_previous_transcriptions(self):
        if os.path.exists(self.transcription_file):
            with open(self.transcription_file, "r") as f:
                return f.read().strip()
        return ""
