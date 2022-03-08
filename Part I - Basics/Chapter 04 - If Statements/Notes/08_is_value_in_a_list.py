"""
Sometimes, you may wish to check whether a new username exists in a list of current usernames, 
before completing somebody's registration on a website. There are of course other situations in which you may wish
to check whether a list constains a specific value before taking an action. For these situations, we use 'in'.
"""

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if ('mushrooms' in requested_toppings):
    print(True)
else:
    print(False)


if ('pepperoni' in requested_toppings):
    print(True)
else:
    print(False)


"""
Sometimes, however, it's important to know if a value does not appear in a list. For this situation, you can use 'not in'.
Usage includes checking if a user has previously been banned, before allowing them to submit a comment.
"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish!')
