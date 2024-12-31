import subprocess
import os
import voice_input, speech_output

def determine_app():
    speech_output.speak("what application would you like to open")
    user_command = voice_input.capture_voice()
    if "code" in user_command:
        vscode_path = r"C:\Users\Sparrow\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        app_path = vscode_path
        return app_path
def open_application(app_path):
    # Path to the Visual Studio Code executable
    
    # Check if the file exists
    if os.path.exists(app_path):
        subprocess.Popen(app_path)
    else:
        print("Visual Studio Code not found at the specified path.")

# Call the function to open VS Code

open_application(determine_app())