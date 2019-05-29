favourite_places = {
    'sarah': ['england', 'belgium'],
    'jono': ['japan', 'spain', 'france'],
    'josh': ['belgium']
}


for name, locations in favourite_places.items():
    print(name.title() + ' would really love to visit:')
    for location in locations:
        print('\t' + location.title())
