filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\guest_book.txt"
more_guests = True

with open(filename, 'a') as file_object:
    while more_guests:
        guest_name = input(
            "Welcome to our establishment! May I please have your name? ")
        file_object.write(guest_name.title() + '\n')

        repeat = input("Are there any more guests?(yes/no): ")
        if repeat == 'no':
            break

print("Thank you for your input.")
