import random
from datetime import datetime


# Current Date and Time
def get_curent_time():
      """
      Returns the current date and time
      """
      return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

# Dice roll between 1 to 6
def roll_dice():
      """
      Returns a random number between 1 and 6
      """
      return random.randint(1, 6)


# Generate random password of any length
def generate_password(length : int)-> str:
      """
      Generates a random password of the specified length
      """
      letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
      password = ''.join(random.choice(letters) for i in range(length))
      return password
      











