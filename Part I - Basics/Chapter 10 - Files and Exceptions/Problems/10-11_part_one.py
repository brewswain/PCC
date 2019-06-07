import json

user_number = input("What is your favorite number? ")

filename = 'favourite_number.json'
with open(filename, 'w') as file_object:
    json.dump(user_number, file_object)
    print("Your favorite number is now seared into my memory banks!")
