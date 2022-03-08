filename = r'Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\guest.txt'
guest_name = input("What's your name? ")

with open(filename, 'a') as file_object:
    file_object.write(guest_name.title() + "\n")
