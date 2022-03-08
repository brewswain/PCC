"""
You can prompt for as much input as you need in each pass through a while loop. 
Let's make a polling program in which each pass through the loop prompts 
for the participant's name and response.

We'll store the data we gather in a dictionary, because we want to connect each
response with a particular user:
"""

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + '.')

"""
The program first defines an empty dictionary(responses) and sets a 
flag (polling_active) to indicate that polling is active. As long as
polling_active is True, Python will run the code in the while loop.

Within the loop, the user is prompted to enter their username and
a mountain they'd like to climb. That info is stored in the responses
dictionary(line 21), and the user is asked whether or not to keep the
poll running. 

If they enter yes, the program enters the while loop again. If they 
enter no, the polling_active flag is set to False, the while loop
stops running, and the final code block(line 30) displays the results
of the poll.
"""
