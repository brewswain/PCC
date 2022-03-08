number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + ' is a multiple of 10! huzzah!')
else:
    print('NOPE')
