from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from the .env file
load_dotenv()

# Create a client that communicates with Ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Send a question to the AI model
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Explain AI in 200 words"
        }
    ]
)

# Display the response
print(138*"=")
print(response.choices[0].message.content)
print(138*"=")



#git add .
#git commit -m "Your commit message"
#git push
