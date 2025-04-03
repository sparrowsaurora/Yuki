from personality.personality import Personality
from ollama import chat, ChatResponse
import time

class Text_Response:
    def __init__(self):
        self.chat_log = []  
        self.FILE_PATH = "input_control/stt_output.txt"
        self.SYSTEM_CONTEXT = Personality.mommy()

    def generate_response(self, prompt):
        if not prompt.strip():
            return "I didn't hear anything, please try again."

        # Get conversation history from file
        conversation_history = self.get_conversation_history()

        final_prompt = f"{self.SYSTEM_CONTEXT}\n\n{conversation_history}\nUser: {prompt}\nYuki:"
        response: ChatResponse = chat(
            model='llama3.2:1b', 
            messages=[{'role': 'user', 'content': final_prompt, 'stream': False}]
        )

        if not response:
            response = "Hmm, I couldn't think of anything. Can you ask something else?"

        response = response.message.content
        self.save_response(response)
        return response

    def get_conversation_history(self, max_lines=10):
        '''
        Read past transcriptions and get the last few exchanges.
        '''
        try:
            with open(self.FILE_PATH, "r") as file:
                lines = file.readlines()
                return "".join(lines[-max_lines:]).strip()
        except FileNotFoundError:
            return ""

    def save_response(self, response):
        '''
        Save Yuki's response to maintain conversation history.
        '''
        with open(self.FILE_PATH, "a") as f:
            f.write(f"Yuki: {response}\n")

    def main(self):
        '''
        Continuously listen and respond.
        '''
        try:
            transcription = self.get_conversation_history(max_lines=1)
            print(f"You: {transcription}")

            if transcription:
                response = self.generate_response(transcription)
                print(f"Yuki: {response}")

        except KeyboardInterrupt:
            print("Stopped watching file.")
