# Modify 10-8.py to fail silently if any file is missing.


def list_pets(filename):
    """List the pet breeds contained in 2 separate files."""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content)


filenames = [r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\Problems\Files\cats.txt",
             "dogs.txt"]
for filename in filenames:
    list_pets(filename)
