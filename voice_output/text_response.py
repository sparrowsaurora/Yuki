from personality.personality import Personality
from ollama import chat, ChatResponse
import time

class Text_Response:
    def __init__(self):
        self.chat_log = []  # Store conversation history
        self.FILE_PATH = "input_control/stt_output.txt"
        # System instructions for the model (personalize the assistant's tone and behavior)
        self.SYSTEM_CONTEXT = Personality.mommy()

    def generate_response(self, prompt):
        '''
        Generate a coherent response based on user input and previous chat history.
        '''
        if not prompt.strip():
            return "I didn't hear anything, please try again."

        # Limit chat history to the last 5 exchanges to maintain context
        chat_history = "\n".join(self.chat_log[-5:])

        # Combine system context with the chat history and user prompt
        final_prompt = f"{self.SYSTEM_CONTEXT}\n\n{chat_history}\nUser: {prompt}\nYuki:"

        # Tokenize the prompt and generate a response
        response: ChatResponse = chat(
            model = 'llama3.2:1b', 
            messages = [
                {
                    'role': 'user',
                    'content': final_prompt,
                    'stream': False,
                },
            ]
        )
        # Decode the response and clean it

        # Ensure the response makes sense and isn't empty
        if not response:
            response = "Hmm, I couldn't think of anything. Can you ask something else?"

        response = response.message.content
        return response

    def clean_prompt(self, prompt):
        '''
        Clean the user input to ensure proper formatting.
        '''
        prompt = prompt.strip()
        if not prompt.endswith(('.', '?', '!')):
            prompt += '.'
        return prompt.capitalize()

    def watch_file(self):
        '''
            Continuously watch a file for new content
        '''
        with open(self.FILE_PATH, 'r') as file:
            file.seek(0, 2) # Go to the end of the file
            while True:
                line = file.readline()
                if line:
                    yield line.strip()
                time.sleep(0.1)

    def main(self):
        # Start a conversation loop
        while True:
            try:
                for transcription in self.watch_file():
                    print(f"You: {transcription}")
                    transcription = self.clean_prompt(transcription)
                    response = self.generate_response(transcription)
                    print(f"Yuki: {response}")

                    # Update the conversation history with the latest input/output
                    self.chat_log.append(f"User: {transcription}")
                    self.chat_log.append(f"Yuki: {response}")
            except KeyboardInterrupt:
                print("Stopped watching file.")

