prompt = "Good Morning, what's your age?: "
age = int(input(prompt))

active = True
while active:
    if age <= 3:
        print('You get in free!')
        break
    elif age <= 12:
        print("Your ticket costs $10.")
        break
    else:
        print('Your ticket costs $15.')
        break
