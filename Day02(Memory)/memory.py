from openai import OpenAI
from dotenv import load_dotenv
import os

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
msg = []
while True:

    user_input = input("\nYou : ")
    # Save the user's message
    msg.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break
    # generate ai reply
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=msg
    )
    
    ai_reply = response.choices[0].message.content

    print("\nAI :", ai_reply)

    # Save the AI's reply
    msg.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

# Chat History
print("\n*******************Chat History************************")

for m in msg:
    print(f"{m['role']} : {m['content']}")

print("\n*******************End of Chat History******************")