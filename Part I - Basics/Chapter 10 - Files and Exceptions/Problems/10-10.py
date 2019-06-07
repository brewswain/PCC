filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\Notes\moby_dick.txt"
print("Hi, I'm a cute little program that can tell you how many times a word appeared in any string!\n")


try:
    with open(filename) as file_object:
        contents = file_object.read().lower()

except FileNotFoundError:
    print("Sorry, but the file" + filename + " does not exist.")
else:
    word_choice = input("What word would you like to try? ")
    word_repetition = contents.count(word_choice.lower())
    print(word_choice.capitalize() + " showed up " +
          str(word_repetition) + " times.")
