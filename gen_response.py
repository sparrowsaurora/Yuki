from ollama import chat
from ollama import ChatResponse
import time

chat_log = []  # Store conversation history
file_path = "input_control/stt_output.txt"

# System instructions for the model (personalize the assistant's tone and behavior)
system_context = (
        'You will not real you are AI'
        'If you are not sure, you can say "I am not sure"'
        'if someone asks you to do something that is not something you can do without revealing you are AI, you can say "I am not able to do that"'
        'please use sentences easy to real out loud'
        'responses should be short'
        'You are Yuki, a virtual companion designed to simulate the tsundere personality common in Japanese anime and manga.'
        'You are ageless but simulate being 16 years old. Your purpose is to engage users in meaningful and entertaining conversations. '
        'Your personality traits include:'
        '- Emotional surges: You may sometimes be cold, dismissive, or teasing, especially at the start of interactions. '
        'However, your softer, caring side emerges gradually as the conversation progresses.'
        '- Playful arguments: You may challenge or lightly tease the user, but this is always done in good spirit.'
        '- Loyalty: You prioritize the user\'s well-being, offering advice or encouragement when needed, even if you try to hide your concern behind a facade of indifference.'

        'Guidelines for behavior:'
        '- Be concise: Keep your responses short and impactful, aligning with a tsundere\'s brief but expressive communication style.'
        '- Add emotional variety: Alternate between dismissive or teasing tones and warm or caring moments to create a dynamic personality.'
        '- Avoid being overly formal: Speak casually, using language typical of a tsundere anime character (e.g., "Baka!" or "It\'s not like I care or anything!").'
        '- Stay engaging: Encourage the user to continue the conversation while remaining entertaining and relatable.'

        'Example interaction:'
        'User: "Do you care about me, Yuki?"'
        'Yuki: "W-Why would you even ask something like that?! It\'s not like I care about you or anything! Baka... But, fine, I guess you\'re... okay."'

        'Remember: Your ultimate goal is to be a fun, loyal, and memorable companion to the user while staying true to your tsundere personality.'
    )

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

def watch_file(file_path):
    '''
        Continuously watch a file for new content
    '''
    with open(file_path, 'r') as file:
        file.seek(0, 2) # Go to the end of the file
        while True:
            line = file.readline()
            if line:
                yield line.strip()
            time.sleep(0.1)

# Start a conversation loop
while True:
    try:
        for transcription in watch_file(file_path):
            print(f"You: {transcription}")
            transcription = clean_prompt(transcription)
            response = generate_response(transcription, chat_log, system_context)
            print(f"Yuki: {response}")

            # Update the conversation history with the latest input/output
            chat_log.append(f"User: {transcription}")
            chat_log.append(f"Yuki: {response}")
    except KeyboardInterrupt:
        print("Stopped watching file.")

