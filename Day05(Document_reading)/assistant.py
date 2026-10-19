from openai import OpenAI
from dotenv import load_dotenv
import os
import re

from tools import (
    get_current_time,
    roll_dice,
    generate_password,read_text_file)

from tool_manager import execute_tool


def clean_markdown(text):
    """Remove markdown formatting so output is plain text."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)   # **bold**
    text = re.sub(r'\*(.+?)\*', r'\1', text)        # *italic*
    text = re.sub(r'__(.+?)__', r'\1', text)         # __bold__
    text = re.sub(r'_(.+?)_', r'\1', text)           # _italic_
    text = re.sub(r'`(.+?)`', r'\1', text)           # `code`
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)  # headings
    return text


# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}


print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice : ")

messages = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
    }
]


while True:

    user_input = input("\nYou : ")
    # Save the user's message

    text = user_input.lower()

    if text.startswith("summarize "):
        filename = user_input[10:].strip()
        file_content = read_text_file(
    	"Data/" + (filename if filename.lower().endswith('.txt') else filename + '.txt')
	    )

        prompt = f"""
        Summarize the following document.

        Document:

        {file_content}
        """

        # Append to main conversation so the model can recall this later
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

        ai_reply = response.choices[0].message.content
        print("\nAI :", clean_markdown(ai_reply))

        # Save the AI's summary to conversation history
        messages.append({"role": "assistant", "content": ai_reply})
        continue

    if text.startswith("explain"):
        filename = user_input[8:].strip()
        # Ensure .txt extension
        if not filename.lower().endswith('.txt'):
            filename += '.txt'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "Data", filename)
        file_content = read_text_file(file_path)
        if file_content is None:
            print(f"\nAI : Unable to read the file '{filename}'. Please check the filename and try again.")
            continue

        prompt = f"""
        Explain the following document.

        Document:

        {file_content}
        """

        # Append to main conversation so the model can recall this later
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

        ai_reply = response.choices[0].message.content
        print("\nAI :", clean_markdown(ai_reply))

        # Save the AI's explanation to conversation history
        messages.append({"role": "assistant", "content": ai_reply})
        continue

   
      

    tool_result = execute_tool(user_input)

    if tool_result:

        print("\nAI :", tool_result)

        continue

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    print("\nAI :", clean_markdown(ai_reply))

    # Save the AI's reply
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    