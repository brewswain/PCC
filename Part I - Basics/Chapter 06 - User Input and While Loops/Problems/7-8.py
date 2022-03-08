sandwich_orders = ['sub', 'hoagie', 'burger', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("Constructing ordered " + current_order + '.')

    finished_sandwiches.append(current_order)
print("\nThe following sandwich orders are complete:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
