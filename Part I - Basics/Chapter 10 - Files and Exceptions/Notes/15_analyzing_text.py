"""
You can analyze text files containing entire books. Many classic works
of literature are available as simple text files because they are in 
the public domain. The texts used in this section come from Project
Gutenberg. 

Project Gutenberg maintains a collection of literary works that are
available in the public domain, and it's a great resource if you're
interested in working with literary texts in your programming projects.

Let's pull in the text of Alice in Wonderland and try to count the 
numbers of words in the text. We'll use the string method split(), which
can build a list of words from a string. Here's what split() does with
a string containing just the title "Alice in Wonderland:"

========================================
|   >>> title = "Alice in Wonderland"  |
|   >>> title.split()                  |
|   ['Alice', 'in', 'Wonderland']      |
========================================

The split() method separates a string into parts wherever it finds a space
and stores all the parts of the string in a list. The result is a list of
words from the string, although some punctuation may also appear with some
of the words. To count the number of words in Alice ihn Wonderland, we'll 
use split() on the entire text. Then we'll count the items in the list to
get a rough idea of the number of words in the text:
"""


filename = "Python_Crash_Course_WIP/Part I - Basics/Chapter 10 - Files and Exceptions/example files/alice.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = "sorry, the file " + filename + " does not exist."
    print(message)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    filename = 'alice.txt'  # Placed here to make output neater.
    print("The file " + filename + " has about " + str(num_words) + " words.")


"""
We moved the file alice.txt to the correct directory, so the try block will
work this time. At line 41, we take the string contents, which now contains
the entire text of Alice in Wonderland as one long string, and use the split()
method to produce a list of all the words in the book. When we use len() on this
list to examine its length, we get a good approximation of the number of words in
the original string(line 42).

At line 43 we print a statement that reports how many words were found in the 
file. This code is placed in the else block because it will work only if the code 
in the try block was executed successfully. the output tells us how many words are 
in alice.txt:

==================================================
|   # The file alice.txt has about 29465 words.  |
==================================================

The count is a little high because extra information is provided by the publisher in 
the text file used here, but it's a good approximation of the length of Alice in
Wonderland.
"""
