from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import get_curent_time, roll_dice, generate_password
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

# Role selection
roles = {"1":"Act like a maths teacher", "2":"Act like a physics teacher", "3":"Act like a chemistry teacher"}
print("1. Maths teacher")
print("2. Physics teacher")
print("3. Chemistry teacher")

# User input
choice = input("Enter your role : ")

msg = [{"role":"system","content":roles.get(choice,"Act like a maths teacher")}]

while True:

    user_input = input("\nYou : ")
    

    # tool calling

    if "time" in user_input.lower():
        print("\nAI : Current time is : ",get_curent_time())
        continue 
    if "roll dice" in user_input.lower():
        print("\nAI : Dice rolled : ",roll_dice())
        continue 
    if "generate password" in user_input.lower():
        print("\nAI : Password generated : ",generate_password(10))
        continue 
    # Save the user's message
    msg.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    if user_input.lower() == "exit":
        print("\nAI  : Goodbye! Have a great day.")
        break
    # generate ai reply
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=msg
    )
    
    ai_reply = response.choices[0].message.content

    print(f"\nAI :{ai_reply}")

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
