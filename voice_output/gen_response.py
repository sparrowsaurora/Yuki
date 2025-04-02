from personality.personality import Personality
from ollama import chat, ChatResponse
import time

chat_log = []  # Store conversation history
FILE_PATH = "input_control/stt_output.txt"
# System instructions for the model (personalize the assistant's tone and behavior)
SYSTEM_CONTEXT = Personality.tsundere()

def generate_response(prompt, chat_log, system_context):
    '''
    Generate a coherent response based on user input and previous chat history.
    '''
    if not prompt.strip():
        return "I didn't hear anything, please try again."

    # Limit chat history to the last 5 exchanges to maintain context
    chat_history = "\n".join(chat_log[-5:])

    # Combine system context with the chat history and user prompt
    final_prompt = f"{system_context}\n\n{chat_history}\nUser: {prompt}\nYuki:"

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

def clean_prompt(prompt):
    '''
    Clean the user input to ensure proper formatting.
    '''
    prompt = prompt.strip()
    if not prompt.endswith(('.', '?', '!')):
        prompt += '.'
    return prompt.capitalize()

def watch_file(FILE_PATH):
    '''
        Continuously watch a file for new content
    '''
    with open(FILE_PATH, 'r') as file:
        file.seek(0, 2) # Go to the end of the file
        while True:
            line = file.readline()
            if line:
                yield line.strip()
            time.sleep(0.1)

# Start a conversation loop
while True:
    try:
        for transcription in watch_file(FILE_PATH):
            print(f"You: {transcription}")
            transcription = clean_prompt(transcription)
            response = generate_response(transcription, chat_log, SYSTEM_CONTEXT)
            print(f"Yuki: {response}")

            # Update the conversation history with the latest input/output
            chat_log.append(f"User: {transcription}")
            chat_log.append(f"Yuki: {response}")
    except KeyboardInterrupt:
        print("Stopped watching file.")

