# speech_output.py
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Get available voices
    voices = engine.getProperty('voices')
    
    # Set voice to female (usually the second voice in the list)
    for voice in voices:
        if "female" in voice.name.lower():  # check if the voice is female
            engine.setProperty('voice', voice.id)
            break
    else:
        engine.setProperty('voice', voices[1].id)  # default to the second voice
    
    engine.say(text)
    engine.runAndWait()