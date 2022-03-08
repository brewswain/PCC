"""
In the previous example, we informed our users that one of the files was
unavailable. But you don't need to report every exception you catch.
Sometimes you'll want the program to fail silently when nothing  an
exception occurs and continue on as if nothing happened. To make a 
program fail silently, you write a try block as usual, but you explicitly
tell Python to do nothing in the except block. Python has a pass statement
that tells it to do nothing in a block:
"""


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
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
When a FileNotFoundError is raised, the pass statement makes the code in the
except block run, but nothing happens. No traceback is produced, and there's 
no output in response ot the error that was raised. Users see the word counts 
for each file that exists, but they don't see any indication that a file was 
not found:

==========================================================
|   # The file alice.txt has about 29465 words.          |
|   # The file moby_dick.txt has about 214435 words.     |
|   # The file little_women.txt has about 189080 words.  |
==========================================================

The pass statement also acts as a placeholder. It's a reminder that you're
choosing to do nothing at a specific point in your program's execution and 
that you might want to do something there later. For example, in this program
we might decide to write any missing filenames to a file called missing_files.tx.
Our users wouldn't see this file, but we'd be able to read the file and deal with
any missing texts.
"""
