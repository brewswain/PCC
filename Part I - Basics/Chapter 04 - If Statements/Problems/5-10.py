current_users = ['chungus', 'rotund pal',
                 'simple and honest', 'bob', 'xX 420_smoker Xx']
new_users = ['BOB', 'clarence', 'rotund pal', 'beep', 'boop']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, but the username: "' + new_user.lower() +
              '" is already taken, please enter a new one.')
    else:
        print('Welcome to the site!')
