'''
    This file uses OpenAI's Whisper to Create live transcription of speech

    Note:::
        Reduce CHUNK_DURATION for lower latency (will increase CPU usage)

'''

import whisper
import sounddevice as sd
import numpy as np
import queue

#loading whisper module (Choose from tiny, base, small, medium, large)
# we are using Base for best preformance to speed and usage ratio 
model = whisper.load_model("base")

#Setting audio params
SAMPLE_RATE = 16000
CHUNK_DURATION = 3  # seconds
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)

# Queue to store audio chunks
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    '''
        Callback to collect audio chunks
    '''
    if status:
        print(f"Audio error: {status}")
    audio_queue.put(indata.copy())

def process_audio():
    '''
        Process audio from "audio_queue" and transcribe it
    '''
    while True:
        audio_data = audio_queue.get()

        # convert audio => mono and scale to 16-bit
        audio_data = audio_data.mean(axis = 1).astype(np.float32)

        # transcribe via whisper
        result = model.transcribe(audio_data, fp16 = False)
        print(f"Transcription: {result['text']}")

# Start audio
with sd.InputStream(
    samplerate = SAMPLE_RATE,
    channels = 1,
    callback = audio_callback,
    blocksize = CHUNK_SIZE
):
    print("listening for (live) audio. Press Ctrl+C to stop.")
    try:
        process_audio()
    except KeyboardInterrupt:
        print("\nStopping transcription.")