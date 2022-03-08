filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))
