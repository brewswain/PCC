# age = 23
# message = 'Happy ' + age + 'rd Birthday!'
# print(message)

"""
The above code will generate a type error: "Can't convert 'int' object to str implicitly".
This is a type error. It means that python can't recognize the kind of information you're using.
In order to avoid this, you'll need to specify explicitly that you want Python to use the integer as a string.
This can be accomplished by using the str() function.
"""
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)
