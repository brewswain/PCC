def city_details(city, country, population=''):
    """Print out a name of a City, followed by the country it's in."""
    # city_name = input("City name: ")
    # country_name = input("Country name: ")
    if population:
        city_format = city + ", " + country + \
            "." + "\nPopulation: " + str(population)
        return city_format.title()

    else:
        city_format = city + ", " + country + "."
        return city_format.title()


print(city_details('tacarigua', 'trinidad', 7))
