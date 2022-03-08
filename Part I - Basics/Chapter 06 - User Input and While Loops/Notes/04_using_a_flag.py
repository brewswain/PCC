"""
In the previous example in 3_while_loops.py, we had the program perform
certain tasks while a given condition was true. 
But what about more complicated programs in which many different events could 
cause the program to stop running?

For example, in a game, there are multiple events which can end the game.
Running out of lives, running out of time, failing objectives, should all
end the game. It needs to end if any one of these events happen.
In this example, trying to test for all of these conditions with one while
statement becomes difficult.

To solve this, we can define one variable that determines whether or not
the entire program is active. This variable is called a flag.
The flag acts as a signal to the program, and can set it to run while the 
flag is set to True, and stop running when any of several events sets the
value of the flag to False.

As a result, our overall while statement only needs to check whether or not
the flag is currently True.Then, all our other tests to see if an event has
occurred to set the flag to False, can be neatly organised in the rest of the
program.
"""


prompt = '\nTell me something, and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)
