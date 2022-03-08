import json
filename = 'favourite_number.json'


def store_number():
    favourite_number = input("What is your favorite number? ")
    with open(filename, 'w') as file_object:
        json.dump(favourite_number, file_object)
        print("Your favorite number is now seared into my memory banks!")
        return favourite_number


def get_number():
    try:
        with open(filename) as file_object:
            favourite_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favourite_number


def greet_user():

    favourite_number = get_number()
    if favourite_number:
        print("I know your favourite number! It's " + favourite_number + "!")
    else:
        favourite_number = store_number()


greet_user()
