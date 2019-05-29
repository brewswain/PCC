glossary = {
    'tuple': 'an immutable list',
    'key-value': 'data corresponding to a key',
    'string': 'any data enclosed by quotes',
    'integer': 'a numerical value without decimals',
    'python': 'a fantastic language',
    'argument': 'A value passed to a function (or method) when calling the function.',
    'class': 'A template for creating user-defined objects.',
    'function': 'A series of statements which returns some value to a caller.',
    'IDLE': 'An Integrated Development Environment(IDE) for Python.',
    'iterable': 'An object capable of returning its members one at a time.',
}

for word, definition in glossary.items():
    print(word.title() + ': ' + definition.title())
