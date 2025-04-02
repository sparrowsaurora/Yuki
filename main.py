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

import multiprocessing
import os

def run_speech_to_text():
    """
    Run the speech-to-text module from input_control/speech_to_text.py.
    """
    os.system("python input_control/speech_to_text.py")

def run_gen_response():
    """
    Run the response generation module from gen_response.py.
    """
    os.system("python voice_output/gen_response.py")

def main():
    # Create separate processes for each script
    stt_process = multiprocessing.Process(target=run_speech_to_text)
    response_process = multiprocessing.Process(target=run_gen_response)

    # Start the processes
    stt_process.start()
    response_process.start()

    # Wait for the processes to complete
    stt_process.join()
    response_process.join()

if __name__ == "__main__":
    main()
