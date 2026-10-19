# Current Time Tool

from datetime import datetime

def get_current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")



# Random Number Generator tool

import random

def roll_dice():
    """Return a random number between 1 and 6."""

    return random.randint(1, 6)



# Random Password Generator tool

import secrets
import string

def generate_password(length=12):
    """Generate a secure random password."""

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password



# Read text file tool

def read_text_file(file_path):
    """Read the content of a text file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."



# Write text file tool

def write_text_file(file_path, content):
    """Write content to a text file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return "Content written successfully."
    except Exception as e:
        return f"Error: {e}"