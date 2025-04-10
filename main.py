'''
This Is the main function of the program.This is where the Glue code is written.

Here we will give the inputs to modules or the "personality"
'''

# def main():
#     '''
#     This is where the program starts.
#     we will wait for stimuli then collect that data
#     -> normalise then store normalised data
#     -> then pass this data to a module or the personality
#     -> after we get the response we will ask for a vocal response
#     -> we will then play the voice response
#     --> then loop back with previous information in data
#     '''

from input_control.speech_to_text import Speech_to_text
from output.text_response import Text_Response
from output.voice_output import Voice

def main():
    stt = Speech_to_text()
    tr = Text_Response("soft_dom") # takes one arg. Personality name: String

    print("listening...") # notify on startup

    while True: # Space for User view.
        try:
            transcription = stt.get_speech()
            
            if transcription:
                print(f"You: {transcription}") 
                response = tr.generate_response(transcription)
                print(f"Yuki: {response}")
                Voice.speak(response)

        except KeyboardInterrupt:
            print("\nExiting...") # notify on exit
            break

if __name__ == "__main__":
    main()
