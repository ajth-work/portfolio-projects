import os
import duolingo

# Authenticate with Duolingo credentials
duolingo_username = os.environ.get("DUOLINGO_USERNAME")
duolingo_password = os.environ.get("DUOLINGO_PASSWORD")

# Initialize Duolingo API with your credentials
lingo = duolingo.Duolingo(duolingo_username, duolingo_password)

# Retrieve and print user info
def get_duolingo_user_info():
    user_info = lingo.get_user_info()
    print("Duolingo User Info:")
    print(user_info)

# Assuming this function is part of your menu system
def duolingo_menu():
    print("Duolingo Menu")
    print("1. Get User Info")
    choice = input("Select an option: ")

    if choice == "1":
        get_duolingo_user_info()