import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'

    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Hello, is this " + username + "?")
        correct_username = input("(yes/no): ")
        if correct_username.lower() == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
