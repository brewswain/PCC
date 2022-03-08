filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\learning_python.txt"

# Read the entire file

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print('')


# Loop over the file object

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print('')


# Store lines in a list and work with them outside the with block
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
