user_names = []

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user_name.title() + ', thank you for logging in.')
else:
    print('We need to find some users!')
