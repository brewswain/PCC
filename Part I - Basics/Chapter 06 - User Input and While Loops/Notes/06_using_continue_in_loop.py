"""
Instead of breaking out of a loop entirely without executing the 
rest of its code, you can use the continue statement to return to
the beginning of the loop based on the result of a conditional test.

For example, consider a loop that counts from 1 to 10 but prints only
the odd numbers in that range:
"""

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


"""
First, we set current_number to 0. Since it's less than 10, the loop 
starts. Once inside the loop, we increment the count by 1 at line 13,
the current_number == 1. 

The if statement then checks the modulo of current_number and 2.
If the modulo is 0, the continue statement tells Python to ignore
the rest of the loops and return to the beginning. If the current
number is not divisible by 2, the rest of the loop is executed and 
Python prints the current number.
"""
