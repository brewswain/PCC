"""
So far, we've worked with only one piece of user information at a time.
We received the user's input and then printed the input or response to
it. The next time through the while loop, we'd receive another input
value and respond to that.

But to keep track of many users and pieces of information, we'll need
to use lists and dictionaries with our while loops.

A for loop is effective for loooping through a list, but you shouldn't
modify a list inside a for loop because Python will have trouble keeping
track of the items in the list. To modify a list as you work through it,
use a while loop. Using while loops with lists and dictionaries allows you
to collect, store and organise lots of input to examine and report on later.
"""

# Moving Items from One List to Another

"""
COnsider a list of newly registered but unverified users of a website.
After we verify these users, how can we move them to a separate list of
confirmed users? One way would be to use a while loop to pull users from
the list of unconfirmed users as we verify them and then add them to a
separate list of confirmed users. Here's wat that code might look like:
"""

# Start with users that need to be verified
# And an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []


# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

# The while loop runs as long as the list unconfirmed_users is not empty.
while unconfirmed_users:

    # Remove unverified users one at a time from the end of unconfirmed_users.
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())

    # Here,  users last in the unconfirmed_users list will be the first to be removed,
    # stored in current_user, and added to confirmed_users.
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
