"""
Handling errors correctly is especially important when the program
has more work to do after the error occurs. This happens often in
programs that prompt users for input. If the program responds to
invalid input appropriately, it can prompt for more valid input
instead of crashing.

Lets create a simple calculator that does only division:
"""

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break

#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break

#     answer = int(first_number) / int(second_number)
#     print(answer)

"""
This program prompts the user to input a first_number and,
if the user does not enter 'q' to quit, a second_number. We
then divide these two numbers to get an answer. This program
does nothing to handle errors, so asking it to divide by zero
causes it to crash.

It's bad that the program crashed, but it's also not a good
idea to let users see tracebacks. Nontechnical users will be
confused by them, and in a malicious setting, attackers will
learn more than you want them to know from a traceback. For
example, they'll know the name of your program file, and they'll 
see a part of your code that isn't working properly. A skilled 
attacker can sometimes use this information to use against
your code.
"""

# The else Block

"""
We can make this program more error resistant by wrapping the line 
that might produce errors in a try-except block. The error occurs 
on the line that performs the division, so that's where we'll put
the try-except block. This example also includes an else block. 
Any code that depends on the try block executing successfully goes
in the else block:
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

"""
We ask Python to try to complete the division operation in a try
block, which includes only the code that might cause an error.
Any code that depends on the try block succeeding is added to the 
else block. In this case if the division operation is successful,
we use the else block to print the result.

The except block tells Python how to respond when a ZeroDivisionError
arises. If the try statement doesn't succeed because of a division
by zero error,  we print a friendly message telling the user how to
avoid this kind of error. The program continues to run, and the user
never sees a traceback.

The try-except-else block works like this: Python attempts to run the
code in the try statement. The only code that should go in a try statement
is code that might cause an exception to be raised. Sometimes you'll have 
additional code that should run only if the try block was successful; this
code goes into the else block. The except block tells Python what to do in
case  a certain exception arises when it tries to run the code in the try
statement.

Byt anticipating likely sources of errors, you can write robust programs that 
continue to run even when they encounter invalid data and missing resources. 
Your code will be resistant to innocent user mistakes and malicious attacks.
"""
