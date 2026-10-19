# Import the OpenAI library so we can talk to the AI model
from openai import OpenAI

# Import dotenv so we can read secret values (like API keys) from a .env file
from dotenv import load_dotenv

# Import os so we can access environment variables (values stored outside the code)
import os

# Import re (regular expressions) so we can find and remove markdown symbols from text
import re

# Import our custom tools: get time, roll a dice, generate a password, and read a text file
from tools import (
    get_current_time,
    roll_dice,
    generate_password, read_text_file)

# Import our tool manager which decides which tool to run based on user input
from tool_manager import execute_tool


def clean_markdown(text):
    """Remove markdown formatting so output is plain text."""
    # Remove **bold** markers → keep just the word inside
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)   # **bold**
    # Remove *italic* markers → keep just the word inside
    text = re.sub(r'\*(.+?)\*', r'\1', text)        # *italic*
    # Remove __bold__ markers → keep just the word inside
    text = re.sub(r'__(.+?)__', r'\1', text)         # __bold__
    # Remove _italic_ markers → keep just the word inside
    text = re.sub(r'_(.+?)_', r'\1', text)           # _italic_
    # Remove `code` backtick markers → keep just the word inside
    text = re.sub(r'`(.+?)`', r'\1', text)           # `code`
    # Remove heading markers like # or ## at the start of lines
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)  # headings
    return text


# Load the secret values from the .env file (like API keys and model name)
load_dotenv()

# Create a connection to the AI service using the URL and API key from .env
client = OpenAI(
    base_url=os.getenv("BASE_URL"),  # The server address for the AI
    api_key=os.getenv("API_KEY")     # Our secret key to access the AI
)

# Print a welcome banner when the program starts
print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

# Define different assistant personalities the user can choose from
# Each number maps to a different system prompt (AI personality/role)
roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer.",

    # New role: a document reading expert that sticks strictly to what's in the document
    "6": "You are a helpful AI assistant, Who is expert in reading and understanding documents, give clear and concise answers, and don't add any extra information which is not present in the document,if asked something which is not present in the document then say i don't know"
}


# Show the available assistant options to the user
print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")
print("6. Document Reader")  # New option added in this version

# Ask the user to pick one of the options above
choice = input("\nEnter your choice : ")

# Set up the conversation history with the chosen AI personality
# If the user picks an invalid number, default to a generic helpful assistant
messages = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."  # Fallback if invalid choice
        )
    }
]


# Start the main chat loop — keeps running until the user types "quit"
while True:

    # Get the user's message from the keyboard
    user_input = input("\nYou : ")
    # Save the user's message

    # Convert input to lowercase for easy keyword checking
    text = user_input.lower()

    # --- SUMMARIZE COMMAND ---
    # If the user types "summarize <filename>", read the file and ask AI to summarize it
    if text.startswith("summarize "):
        # Extract the filename from the message (everything after "summarize ")
        filename = user_input[10:].strip()

        # Read the file from the "Data/" folder; auto-add .txt if missing
        file_content = read_text_file(
    	"Data/" + (filename if filename.lower().endswith('.txt') else filename + '.txt')
	    )

        # Build a prompt asking the AI to summarize the document
        prompt = f"""
        Summarize the following document.

        Document:

        {file_content}
        """

        # Add the summarize request to the main conversation history
        # This allows the AI to recall the document in follow-up questions
        messages.append({"role": "user", "content": prompt})

        # Send the full conversation to the AI and get a reply
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),  # Use the model name from .env
            messages=messages
        )

        # Extract the AI's reply and clean any markdown symbols from it
        ai_reply = response.choices[0].message.content
        print("\nAI :", clean_markdown(ai_reply))

        # Save the AI's summary to conversation history so it can be referenced later
        messages.append({"role": "assistant", "content": ai_reply})
        continue  # Go back to top of loop and wait for next user input

    # --- EXPLAIN COMMAND ---
    # If the user types "explain <filename>", read the file and ask AI to explain it
    if text.startswith("explain"):
        # Extract the filename from the message (everything after "explain ")
        filename = user_input[8:].strip()

        # Auto-add .txt extension if the user didn't include it
        if not filename.lower().endswith('.txt'):
            filename += '.txt'

        # Build the full absolute path to the file so it works from any directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "Data", filename)

        # Read the contents of the file
        file_content = read_text_file(file_path)

        # If the file couldn't be read, show an error and wait for next input
        if file_content is None:
            print(f"\nAI : Unable to read the file '{filename}'. Please check the filename and try again.")
            continue

        # Build a prompt asking the AI to explain the document
        prompt = f"""
        Explain the following document.

        Document:

        {file_content}
        """

        # Add the explain request to the main conversation history
        # This allows the AI to recall the document in follow-up questions
        messages.append({"role": "user", "content": prompt})

        # Send the full conversation to the AI and get a reply
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),  # Use the model name from .env
            messages=messages
        )

        # Extract the AI's reply and clean any markdown symbols from it
        ai_reply = response.choices[0].message.content
        print("\nAI :", clean_markdown(ai_reply))

        # Save the AI's explanation to conversation history so it can be referenced later
        messages.append({"role": "assistant", "content": ai_reply})
        continue  # Go back to top of loop and wait for next user input

   
      

    # --- TOOL CHECK ---
    # Check if the user's message matches a special tool command (e.g., "what time is it?")
    tool_result = execute_tool(user_input)

    if tool_result:
        # If a tool handled the request, print the result and skip the AI
        print("\nAI :", tool_result)

        continue  # Go back to the top of the loop

    # Add the user's message to the conversation history
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # --- QUIT COMMAND ---
    # If the user types "quit", say goodbye and stop the program
    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    # --- NORMAL CHAT ---
    # Send the full conversation history to the AI and get a reply
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),   # Use the model name from .env
        messages=messages           # Pass the entire chat history for context
    )

    # Extract the AI's reply text from the response
    ai_reply = response.choices[0].message.content

    # Print the AI's reply (with markdown symbols cleaned up)
    print("\nAI :", clean_markdown(ai_reply))

    # Save the AI's reply to the conversation history so it remembers context
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    