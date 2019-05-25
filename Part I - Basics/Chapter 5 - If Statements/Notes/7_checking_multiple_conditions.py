"""
Certain situations may require you to check multiple conditions at the same time.
Sometimes you may wish for two conditions to be True before a function gets called.
Other times, you might wish for just one condition to be met. 
Using the keywords 'and' and 'or' can help in these situations.
"""

# Using 'and' To Check Multiple Conditions

"""
To check if two conditions are both True simultaneously, use the keyword 'and'
to combine the two conditional tests. If each test passes, the expression evaluates 
as True. if either test fails or if both tests fail, the expression evaluates as False.
"""
age_0 = 22
age_1 = 18
print('==============================================================================\n')

if age_0 >= 21 and age_1 >= 21:
    print('Both parties are over 21 years old.')
else:
    print('\nNope (っ´ω`)ﾉ(╥ω╥)')

# The above will return line 21's code: "Nope (っ´ω`)ﾉ(╥ω╥)", as age_1 failed the conditional test.

age_1 = 21
if age_0 >= 21 and age_1 >= 21:
    print('\nBoth parties are now over 21 years old D:\n')
else:
    print('\nNope (っ´ω`)ﾉ(╥ω╥)')

# Now that we edited age_1 to be 21 and both tests now pass, if statement executes.

"""
To improve readability, we can wrap parantheses around the individual tests, but they're not required.
eg:
if (age_0 >= 21) and (age_1 >= 21):
"""


# Using 'or' to Check Multiple Conditions

"""
The keyword 'or' allows you to check multiple conditions, but if either, or both, of the individual tests pass,
the expression will evaluate as True. An 'or' expression will only fail when both tests fail.
"""

age_0 = 22
age_1 = 18
print('==============================================================================\n')
if (age_0 >= 21) or (age_1 >= 21):

    print('Both parties are over 21 years old.\n')
else:
    print('\nNope (っ´ω`)ﾉ(╥ω╥)')

# The above will return line 52's code, as, even though age_1 is <21, age_0 passes the test.

age_0 = 20
if (age_0 >= 21) or (age_1 >= 21):

    print('Both parties are over 21 years old.\n')
else:
    print('Nope (っ´ω`)ﾉ(╥ω╥)\n')

# Now that both age_0 and age_1 are below 21, line 64 will execute, as the conditional test returns as False.
