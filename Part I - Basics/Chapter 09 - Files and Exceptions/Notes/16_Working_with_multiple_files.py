"""
Let's add more books to analyze. But before we do, let's move the bulk of
this program to a function called count_words(). By doing so, it will be
easier to run the analysis for multiple books:
"""


# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         message = "Sorry, the file " + filename + " does not exist."
#         print(message)
#     else:
#         # Count approximate number of words in the file.
#         words = contents.split()
#         number_words = len(words)
#         print("The file " + filename + " has about " +
#               str(number_words) + " words.")

# filename = "alice.txt"
# count_words(filename)

"""
We can now write a simple loop to count the words in any text we want to analyze.
We do this by storing a the names of the files we want to analyze in a list, and
then we call count_words() for each file in the list. We'll try to count the 
words for Alice in Wonderland, Siddhartha, 
 Dick, and Little Women. 
siddharta.txt has been intentionally lef out of the directory, so we can see how 
well our program handles a missing file:
"""


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " does not exist."
        print(message)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has about " +
              str(number_words) + " words.")


# Please execute this program using an external terminal to avoid false file not found errors.
filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


"""
The missing siddhartha.txt file has no effect on the rest of the program's execution:

==========================================================
|   # The file alice.txt has about 29465 words.          |
|   # Sorry, the file siddhartha.txt does not exist.     |
|   # The file moby_dick.txt has about 214435 words.     |
|   # The file little_women.txt has about 189080 words.  |
==========================================================

Using the try-except block in this example provides two significant advantages. We
prevent our users from seeing a traceback, and we let the program continue analyzing
the texts it's able to find. If we don't catch the FileNotFoundError that siddhartha.txt
raised, the user would see a full traceback, and the program would stop running after 
trying to analyze Siddhartha. It would never analyze Moby Dick or Little Women.
"""
