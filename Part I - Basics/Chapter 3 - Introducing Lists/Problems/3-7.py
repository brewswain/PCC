guests = ['waddle dee', 'kirby', 'marx', 'meta knight', 'florence', 'magolor']
guests_length = len(guests)
print('Hey, it turns out that I can only invite 2 people, sorry :(\n')

for guest in range(4):
    popped_guest = guests.pop()
    print("Sorry " + popped_guest.title() +
          ", but I can't invite you to dinner any more ;a;")

guests_length = 2
if guests_length <= 2:
    for guest in guests:
        print('Hey ' + guest.title() + ', I still got space for you!')

del guests[1]
del guests[0]
print(guests)
