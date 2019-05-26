guests = ['kirby', 'waddle dee', 'florence']

for guest in guests:
    print('Hey ' + guest.title() + ', I am having a dinner tonight, pull through!')

print('\nI just got a bigger table, so I can invite more people! \n')

guests.insert(0, 'meta knight')
guests.insert(2, 'marx')
guests.append('magolor')


for guest in guests:
    print('Hey ' + guest.title() + ', I am having a dinner tonight, pull through!')
