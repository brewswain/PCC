print("Input 2 numbers, and I'll add them for you.")
print("Press 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        solution = int(first_number) + int(second_number)
    except ValueError:
        print("Please use numbers only.")
    else:
        print(solution)
