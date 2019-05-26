# In Python, anything inside quotes is considered a string. You can use single or double quotes, increasing flexibility

print("One of Python's strengths is its diverse and supportive community.")
print('I told my friend, "Python is insane!"')


# Changing Case in a String with Methods

name = 'aDa woNg'

print(name.title())
print(name.upper())
print(name.lower())

"""
The lower() method is super useful for storing data. You generally don't want ot trust the capitalization
that your users provide, so you can convert strings to lowercase before storing them. Then, when calling the info,
you can use the case that makes the most sense in the situation.
"""


# Combining/Concatenating Strings

first_name = 'ada'
last_name = 'wong'
full_name = first_name + ' ' + last_name
message = 'Hello, ' + full_name.title()

print(message)
