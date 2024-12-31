import speech_recognition as sr
import notebook as nb
from datetime import datetime

# Initialize the speech recognition engine
r = sr.Recognizer()

# Create a new notebook
notebook = nb.Notebook()

while True:
    # Record audio input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to transcribe the audio
    try:
        text = r.recognize_google(audio, language="en-US")
        print("You said:", text)

        # Create a new note and add it to the notebook
        note = nb.Note(title=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), content=text)
        notebook.add_note(note)

        # Print the updated notebook
        print("\nCurrent Notebook:")
        for note in notebook.notes:
            print(note.title)
            print(note.content)

    # Handle errors
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.ElapsedTimeError:
        print("Sorry, audio recording timed out.")
    except Exception as e:
        print("Error:", str(e))

    # Ask if you want to continue recording
    response = input("Do you want to take another note? (y/n): ")
    if response.lower() != "y":
        break