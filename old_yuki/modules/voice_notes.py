import voice_input, speech_output
import pyaudio
import wave
import keyboard  # Install with: pip install keyboard
import os  # Import os to manage file paths

# Define the directory where voice notes will be saved
voice_notes_dir = os.path.join(os.path.dirname(__file__), 'voice_notes_dir')

# Ensure the directory exists
if not os.path.exists(voice_notes_dir):
    os.makedirs(voice_notes_dir)

# Function to record audio and save it as a .wav file in voice_notes_dir
def record_audio_wav(filename, rate=44100, chunk=1024):
    """
    Records audio from the microphone and saves it as a .wav file in voice_notes_dir.
    - filename: The name of the output file without extension.
    - rate: The sample rate of the recording (default: 44100 Hz).
    - chunk: The number of frames per buffer (default: 1024).
    """
    # Set up audio format parameters
    audio_format = pyaudio.paInt16  # 16-bit resolution
    channels = 1                    # Mono audio
    sample_rate = rate               # 44.1kHz sample rate
    chunk_size = chunk               # 1024 samples per chunk

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Start recording
    print("Recording... Press Enter to stop.")
    stream = p.open(format=audio_format, channels=channels,
                    rate=sample_rate, input=True,
                    frames_per_buffer=chunk_size)

    frames = []  # List to store the audio data chunks

    try:
        # Continuously read audio data until the Enter key is pressed
        while True:
            if keyboard.is_pressed('enter'):  # Stop recording when Enter key is pressed
                print("Recording stopped.")
                break
            data = stream.read(chunk_size)  # Read a chunk of data from the stream
            frames.append(data)  # Append the data to the frames list
    except KeyboardInterrupt:
        print("Recording interrupted.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Construct full file path
    file_path = os.path.join(voice_notes_dir, f"{filename}.wav")

    # Save the recorded audio as a .wav file
    with wave.open(file_path, "wb") as wf:
        wf.setnchannels(channels)  # Set the number of channels (mono)
        wf.setsampwidth(p.get_sample_size(audio_format))  # Set the sample width
        wf.setframerate(sample_rate)  # Set the frame rate (sample rate)
        wf.writeframes(b''.join(frames))  # Write the audio frames to the file

    print(f"Audio saved as {file_path}")

# Main function to handle voice note actions (recording or opening notes)
def voice_notes_main():
    while True:
        """
        Main function to manage voice notes. It prompts the user to either:
        - Record a new voice note.
        - Open an existing voice note.
        """
        speech_output.speak(" -- Are you trying to record or open a voice note?")
        user_command = voice_input.capture_voice()  # Capture user command through voice input
        if "exit" in user_command or "quit" in user_command:
            break

        # If the user wants to record a new voice note
        
        elif "record" in user_command:
                speech_output.speak(" -- What shall we name this file?")
                filename = voice_input.capture_voice()  # Capture the file name through voice input
                
                # Handle the case where the filename might already exist or user wants to browse
                if "current" in filename or "index" in filename:
                    for file in os.listdir(voice_notes_dir):  # List all existing .wav files in the voice_notes_dir
                        if file.endswith(".wav"):
                            print(file)
                else:
                    # Check if file already exists
                    if os.path.exists(os.path.join(voice_notes_dir, f"{filename}.wav")):
                        speech_output.speak(" -- File already exists. Would you like to overwrite it?")
                        user_command = voice_input.capture_voice()
                        if "yes" in user_command or "overwrite" in user_command:
                            speech_output.speak(" -- Overwriting existing file.")
                            record_audio_wav(filename)
                        elif "no" in user_command:
                            speech_output.speak(" -- Recording cancelled.")
                    else:
                        # Loop until the user confirms the file name
                        while True:
                            speech_output.speak("Confirm file name is " + filename)
                            filename_confirmation = voice_input.capture_voice()  # Confirm the filename through voice input
                            if "yes" in filename_confirmation:
                                record_audio_wav(filename)  # Start recording the voice note
                                break
                            else:
                                speech_output.speak(" -- What shall we name this file?")  # Ask for filename again if not confirmed
                                filename = voice_input.capture_voice()

        # If the user wants to open or read an existing voice note
        elif "open" in user_command or "read" in user_command:
            speech_output.speak(" -- Which note would you like to open?")
            filename = voice_input.capture_voice()  # Capture the name of the file to open
            
            # If the user wants to read a text note
            if "read" in filename:
                speech_output.speak(" -- Reading note...")
                file_path = os.path.join(voice_notes_dir, f"{filename}.txt")
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        speech_output.speak(f.read())  # Read the text note aloud
                    speech_output.speak(" -- Note read.")
                else:
                    speech_output.speak(f" -- No text note found with name {filename}.")
            
            # If the user wants to browse the list of saved .wav files
            elif "index" in filename:
                for file in os.listdir(voice_notes_dir):  # List all existing .wav files in the directory
                    if file.endswith(".wav"):
                        print(file)



