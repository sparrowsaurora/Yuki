# Voice Output

## File Paths

    voice_output/          # Controls the voice output
     └── voice_output.md   # Description of the 'voice_output' directory

https://platform.openai.com/docs/guides/text-to-speech

from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
model="tts-1",
voice="alloy",
input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")

open AI's TTS is pretty cheap (~ $0.15 for 10 minutes)

but Elevenlabs voice has a Startup program with similar costs. plus i want to work with elevenlabs more
