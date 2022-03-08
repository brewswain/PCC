# Simulate a friendly error generated if program can't find file.


def list_pets(filename):
    """List the pet breeds contained in 2 separate files."""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        message = "Sorry, but the file " + filename + " does not exist."
        print(message)
    else:
        print(content)


filenames = [r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\Problems\Files\cats.txt",
             "dogs.txt"]
for filename in filenames:
    list_pets(filename)
