favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
pollers = ['sarah', 'jono', 'josh', 'phil', 'edward']

print('\n')
for name in favourite_languages.keys():
    if name in pollers:
        print(name.title() + ', thank you so much for doing our poll!')

print('\n')
for name in pollers:
    if name not in favourite_languages:
        print(name.title() + ', feel free to take our poll :3')
