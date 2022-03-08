"""
Every while loop needs a way to stop running so it won't continue
to run forever. For example, this counting loop should count from 
1 to 5:
"""

x = 1
while x <= 5:
    print(x)
    x += 1

"""
But, if we accidentally omit the line "x += 1", the loop will
run forever:

x = 1
while x <= 5:
    print(x)


Now the value of x will start at 1 but never change. As a result, the
conditional test x <= 5 will always evaluate to True and the while loop
will run forever, printing a series of 1s, like this:

1
1
1
1
1
1


If your program gets stuck in an infinite loop, press CTRL-C.
Test every while loop and make sure the loop stops when you expect it to.
If you want your program to end when the user enters a certain input value,
run the program and enter that value.

If the program doesn't end, scrutinize the way your program handles tha value 
that should cause the loop to exit. Make sure at least one part of the program 
can make the loop's condition False or cause it to reach a break statement.
"""
