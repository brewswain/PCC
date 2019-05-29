cities = {
    'tacarigua': {
        'country': 'trinidad',
        'population': '2',
        'fact': 'There has never been a police station in Tacarigua.',
    },

    'tampa': {
        'country': 'america',
        'population': '385,430',
        'fact': "Tampa is home to the worlds longest continuous sidewalk.",
    },

    'melbourne': {
        'country': 'australia',
        'population': '4.443 million',
        'fact': 'Melbourne is the fox capital of the world.',
    },
}

for city, city_info in cities.items():
    print('\nCity: ' + city.title())
    print('Country: ' + city_info['country'].title())
    print('Population: ' + city_info['population'])
    print('Fact: ' + city_info['fact'])
