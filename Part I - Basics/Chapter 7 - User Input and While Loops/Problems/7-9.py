sandwich_orders = ['pastrami', 'sub', 'hoagie',
                   'pastrami', 'burger', 'pastrami', 'grilled cheese']
finished_sandwiches = []

print("We're out of pastrami, sorry :(\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("Constructing ordered " + current_order + '.')

    finished_sandwiches.append(current_order)
print("\nThe following sandwich orders are complete:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
