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
from voice_output.text_response import Text_Response

def main():
    stt = Speech_to_text()
    yuki = Text_Response()

    print("Yuki is listening... Speak now.")

    while True:
        try:
            transcription = stt.get_speech()
            
            if transcription:
                print(f"You: {transcription}")
                response = yuki.generate_response(transcription)
                print(f"Yuki: {response}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
