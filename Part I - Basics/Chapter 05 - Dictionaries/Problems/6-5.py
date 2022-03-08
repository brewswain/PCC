rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'ganges': 'india',
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title())
print('\n')

print('These are some of the most famous rivers:')
for river in rivers.keys():
    print(river.title())
print('\n')

print("These countries lie host to some of the world's biggest rivers:")
for country in rivers.values():
    print(country.title())
