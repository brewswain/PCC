# How the input() Function Works

"""
The input() function pauses your program and waits for the user to enter
some text. Once Python receives the user's input, it stores it in a variable
to make it convenient for you to work with.
"""

message = input('Tell me something, and I will repeat it back to you: ')
print(message)


# Writing Clear Prompts

"""
Each time you use the input() function, you should include  a clear,
easy-to-follow prompt that tells the use exactly what kind of information
you're looking for. Any statement that tells the user what to enter works.
"""

name = input('Please enter your name: ')
print('Hello, ' + name.title() + '!')


"""
Sometimes, you'll want to write a prompt that's longer than one line. You
can store your prompt in a variable and pass that variable to the input() function.
This allows you to build your prompt over several lines, then write a clean input()
statement.
"""

prompt = 'If you tell me who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('Hello', name.title() + '!')
