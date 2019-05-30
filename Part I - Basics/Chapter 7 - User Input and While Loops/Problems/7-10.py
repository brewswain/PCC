responses = {}

polling_active = True

while polling_active:
    name = input("\nwhat is your name? ")
    response = input(
        "\nIf you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Is there somebody else who wants to respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name.title() + " wishes to visit " +
          response.title() + " in their lifetime.")
B
