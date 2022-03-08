prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'done' to begin making the pizza.) "

active = True

while active:
    message = input(prompt)

    if message == 'done':
        print("Making your pizza now, please wait.")
        active = False

    else:
        print("Ok, we'll add " + message + " to your pizza.")
