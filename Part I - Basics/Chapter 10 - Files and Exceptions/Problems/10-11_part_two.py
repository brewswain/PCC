import json

filename = 'favourite_number.json'
with open(filename) as file_object:
    favourite_number = json.load(file_object)
    print("I know your favourite number! It's " + favourite_number + "!")
