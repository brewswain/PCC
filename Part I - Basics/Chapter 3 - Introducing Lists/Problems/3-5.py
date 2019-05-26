guests = ['kirby', 'john', 'florence']

for guest in guests:
    print('Hey ' + guest.title() + ', I am having a dinner tonight, pull through!')
print("\nJohn can't make it :( \n")

guests[1] = 'waddle dee'

for guest in guests:
    print('Hey ' + guest.title() + ', I am having a dinner tonight, pull through!')
