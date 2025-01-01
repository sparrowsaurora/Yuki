from modules import voice_input, speech_output
import main
# Dictionary to map spoken phrases to symbols
word_to_symbol = {
    "open bracket": "(",
    "close bracket": ")",
    "open curly bracket": "{",
    "close curly bracket": "}",
    "open square bracket": "[",
    "close square bracket": "]",
    "equals": "=",
    "colon": ":",
    "semicolon": ";",
    "quote": "\"",
    "single quote": "'",
    "comma": ",",
    "dot": ".",
    "plus": "+",
    "minus": "-",
    "dot point": " > ",
    "times": "*",
    "divide": "/",
    "new line": "\n",
    "comment" : "#",
}

def write_code_file():
    speech_output.speak("what should we call this notes file?")
    filename = voice_input.capture_voice()
    with open(f"{filename}.md", "a") as file:
        print(f"File {filename}.md written successfully!")
        speech_output.speak(f"File {filename}.md written successfully!")
    while True:
        write_code_file_from_voice(filename)
        

def write_code_file_from_voice(filename):
    voice_text = voice_input.capture_voice()
    if "end session" in voice_text:
        main.main()
    if voice_text:
        interpreted_code = interpret_voice_to_code(voice_text)
        with open(f"{filename}.md", "a") as file:
            file.write(interpreted_code)
        print(f"Code written to {filename}.md successfully!")
        print(f"Your code:\n{interpreted_code}")

# Example usage
if __name__ == "__main__":
    write_code_file_from_voice("example")

def interpret_voice_to_code(voice_text):
    # Split the voice input into words or phrases
    words = voice_text.lower().split()
    
    # Initialize an empty list to store interpreted code
    code = []
    
    i = 0
    while i < len(words):
        phrase = words[i]
        
        # Check for two-word phrases (like "open bracket")
        if i < len(words) - 1:
            two_word_phrase = f"{words[i]} {words[i+1]}"
            if two_word_phrase in word_to_symbol:
                code.append(word_to_symbol[two_word_phrase])
                i += 2
                continue
        
        # Check for single-word symbols (like "comma")
        if phrase in word_to_symbol:
            code.append(word_to_symbol[phrase])
        else:
            code.append(phrase)  # Append the word as it is if no symbol matches
        
        i += 1
    
    return " ".join(code)

