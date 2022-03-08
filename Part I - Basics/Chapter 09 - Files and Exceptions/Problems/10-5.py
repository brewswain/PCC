filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\why_program.txt"

print("Feel free to type 'quit' at any time to close this program." + '\n')

while True:
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason.capitalize() + '\n')
