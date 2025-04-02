'''
    This file uses OpenAI's Whisper to Create live transcription of speech

    Note:::
        Reduce CHUNK_DURATION for lower latency (will increase CPU usage)

'''

import whisper
import sounddevice as sd
import numpy as np
import queue

class Speech_to_text:
    def __init__(self):
        #loading whisper module (Choose from tiny, base, small, medium, large)
        # we are using Base for best preformance to speed and usage ratio 
        self.model = whisper.load_model("base")

        #Setting audio params
        self.SAMPLE_RATE:int = 16000
        self.CHUNK_DURATION:int = 3  # seconds
        self.CHUNK_SIZE:int = self.SAMPLE_RATE * self.CHUNK_DURATION

        # Queue to store audio chunks
        self.audio_queue = queue.Queue()

    def audio_callback(self, indata, frames, time, status):
        '''
            Callback to collect audio chunks
        '''
        if status:
            print(f"Audio error: {status}")
        self.audio_queue.put(indata.copy())

    def process_audio(self):
        '''
            Process audio from "audio_queue" and transcribe it
        '''
        while True:
            audio_data = self.audio_queue.get()

            # convert audio => mono and scale to 16-bit
            audio_data = audio_data.mean(axis = 1).astype(np.float32)

            # transcribe via whisper
            result = self.model.transcribe(audio_data, fp16 = False)
            with open("input_control/stt_output.txt", "a") as f:
                f.write(result['text'] + "\n")

    def main(self):
        # Start audio
        with sd.InputStream(
            samplerate = self.SAMPLE_RATE,
            channels = 1,
            callback = self.audio_callback,
            blocksize = self.CHUNK_SIZE
        ):
            print("listening for (live) audio. Press Ctrl+C to stop.")
            try:
                self.process_audio()
            except KeyboardInterrupt:
                print("\nStopping transcription.")