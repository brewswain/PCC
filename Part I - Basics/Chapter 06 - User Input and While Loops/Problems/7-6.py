prompt = "\nWhat toppings would you like on your pizza?(Maximum 5.)"
prompt += "\n(Enter 'done' to begin making the pizza.) "
toppings = 0


while toppings <= 5:
    message = input(prompt)

    if message == 'done':
        print("Making your pizza now, please wait.")
        break

    else:
        print("Ok, we'll add " + message + " to your pizza.")
        toppings += 1

        if toppings >= 5:
            input(
                "\nMaximum toppings reached!")
