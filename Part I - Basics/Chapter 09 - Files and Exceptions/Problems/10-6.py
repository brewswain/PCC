print("Input 2 numbers, and I'll add them for you.")

first_number = input("First number: ")
second_number = input("Second number: ")

try:
    solution = int(first_number) + int(second_number)
except ValueError:
    print("Please use numbers only.")
else:
    print(solution)
