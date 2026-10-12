# Import the OpenAI class from the openai library to interact with the API
from openai import OpenAI
# Import the load_dotenv function to read key-value pairs from a .env file and set them as environment variables
from dotenv import load_dotenv
# Import the os module to interact with the operating system, like reading environment variables
import os 

# Call load_dotenv to load environment variables from a .env file into the os environment
load_dotenv()

# Initialize the OpenAI client with configuration parameters
client = OpenAI(
      # Set the base_url for the OpenAI client using the BASE_URL environment variable
      base_url = os.getenv("BASE_URL"),
      # Set the api_key for the OpenAI client using the API_KEY environment variable
      api_key = os.getenv("API_KEY")
)

# Print a line of 100 equals signs to format the console output
print("="*100)
# Print the title of the application to the console
print("         My AI Assistant")
# Print another line of 100 equals signs to complete the formatting
print("="*100)

# Start an infinite loop to continuously accept user input and generate responses
while True:

      # Prompt the user for input and store it in the user_input variable
      user_input = input("\nYou :  ")

      # Check if the user's input, converted to lowercase, is exactly "quit"
      if user_input.lower() == "quit":
            # Print a goodbye message if the user wants to quit
            print("\nAI : Goodbye! ")
            # Break out of the infinite loop, terminating the program
            break
      # If the user did not type "quit", execute this block
      else :
            # Make an API call to the OpenAI chat completions endpoint to generate a response
            response = client.chat.completions.create(
                  # Specify the AI model to use, retrieving the value from the MODEL environment variable
                  model = os.getenv("MODEL"),
                  # Provide the conversation history, which currently only contains the user's latest input
                  messages = [
                        # Define a single message from the "user" role
                        {"role" : "user",
                        # Set the content of the message to what the user typed
                        "content" : user_input}
                  ]
            )

      # Print the AI's response to the console, extracting the text content from the API response object
      print("\nAI : ", response.choices[0].message.content)


# git add . && git commit -m "System prompt done" && git push
