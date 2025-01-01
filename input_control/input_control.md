# Input Control

## Idea

this is where inputs like the user's voice, gestures, or other forms of user input are processed and interpreted to determine the system's response.  
Inputs may include:  

- Voice commands (e.g. "turn on the lights")
- Gestures (e.g. hand or finger movements)
- Keystrokes (e.g. typing on a keyboard)
- Biometric data (e.g. facial recognition)
- Environmental data (e.g. temperature, humidity, light levels)

## File Paths

    input_control/                  # Controls inputs
     ├── input_control.md           # Description of the 'input_contol' directory
     ├── command_normalisation.py   # determination and normalisation of commands
     ├── emotional_analysis.py     # determination of emotion and tone
     └── speech_to_text.py          # speech to tech via openAI whisper

## To Implement

### Inputs

Speech To Text (STT) via OpenAI Whisper  
Computer Vision via OpenCV  
Keystroke Recognition via PyAutoGUI  
Environmental data via PySense, requests to websites and Arduino  

### Catagorisation

Use Inputs to determine if data is a command or speech to respond to

### If speech => Emotional analysis

analyse tone and emotion of conversation for response  

### If command => Normalisation

AI models require data to be in a specific format, so we need to normalise the inputs to match  
AI catagorisation of inputs to match the AI models' expected inputs for STT data  

### Format Data

Format data for Modules directory
