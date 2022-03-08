favourite_numbers = {'bob': 5, 'sarah': 13, 'jim': 42, 'seth': 69, 'cody': 420}

favourite_numbers = {
    'bob': [5, 12, 1],
    'sarah': [37],
    'jim': [32, 95],
    'seth': [2, 55, 32, 5],
    'cody': [69, 420],
}


for name, numbers in favourite_numbers.items():
    print(name.title() + "'s favourite number(s) include:")
    for number in numbers:
        print('\t - ' + str(number))
