locations = ['japan', 'sweden', 'korea', 'iceland', 'norway']

print(locations)
print(sorted(locations))
print(locations)  # proof that the list is still in its original order
print(sorted(locations, reverse=True))
print(locations)  # proof that the list is still in its original order

locations.reverse()
print(locations)
locations.reverse()  # Revert order
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)
