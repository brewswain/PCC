"""
Often, you'll want to start with an existing list and make an entirely new list based on the first one.
To copy a list, you can make a slice that includes the entire original list by omitting the first index
and the second index - [:].

This tells Python to make a slice that starts at the first item and ends with the last item,
producing a copy of the entire list.
For instance, imagine we have a list of our favourite foods and want to make a separate list of foods
that a friend likes. This friend likes everything in our list so far, so we can create their list by copying ours:
"""


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favourite foods are:')
print(my_foods)

print("My friend's favourite foods are:")
print(friend_foods)


"""
To prove that we actually have two separate lists, we'll add a new food to each list,
and show that each list keeps track of the appropriate person's favourite foods:
"""


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('doubles')
friend_foods.append('ice cream')

print('My favourite foods are:')
print(my_foods)

print("My friend's favourite foods are:")
print(friend_foods)


"""
If we simply set 'friend_foods = my_foods', we would not produce two separate lists.
The syntax tells Python to connect the enw variable 'friend_foods' to the list
that's already contained in 'my_foods', so now both variables point to the same list.
The end result would be the appends in lines 32 and 33 would ensure that both lists 
are the same, i.e.

['pizza', 'falafel', 'carrot cake', 'doubles', 'ice cream']
"""
