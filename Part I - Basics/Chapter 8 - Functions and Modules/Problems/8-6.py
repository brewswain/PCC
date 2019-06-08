def city_country(city, country):
    location = city + ', ' + country
    return location.title()


detailed_location = city_country('tacarigua', 'trinidad')
print(detailed_location)
