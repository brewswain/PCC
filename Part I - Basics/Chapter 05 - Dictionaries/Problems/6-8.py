# bob = {'species': 'manatee', 'owner': 'big bob'}
# sully = {'species': 'sloth', 'owner': 'patches'}
# darius = {'species': 'kangaroo', 'owner': 'jack'}


pets = []

pet = {
    'name': 'bob',
    'species': 'manatee',
    'owner': 'big bob',
}
pets.append(pet)

pet = {
    'name': 'sully',
    'species': 'sloth',
    'owner': 'patches',
}
pets.append(pet)


pet = {
    'name': 'darius',
    'species': 'kangaroo',
    'owner': 'jack',
}
pets.append(pet)

for pet in pets:
    print("\nThis is  " + pet['name'].title() + "'s information:")
    for key, value in pet.items():
        print("\t\t" + key.title() + ': ' + value.title())
