"""
    Extra whitespace can be confusing in your programs. 
To programmers, 'python' and 'python ' look the same. But to a program, these are two different strings. 
Python detects the extra space and considers it significant unless told otherwise.
We can deal with whitespace using  strip methods.
"""

# rstrip()

favourite_language = 'python '
favourite_language = favourite_language.rstrip()
print(favourite_language)

# To strip whitespace on the left side of a string, you may use lstrip(). For both sides at once, simply use strip().

favourite_language = ' python'
favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = ' python '
favourite_language = favourite_language.strip()
print(favourite_language)
