"""
A function can return any kind of value you need it to, including 
more complicated data structures like lists and dictionaries. For
example, the following function takes in parts of a name and returns 
a dictionary representing a person:
"""


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
