def describe_city(city_name, country='usa'):
    if country == 'usa':
        print(city_name.title() + " is located in: " + country.upper() + ".")
    else:
        print(city_name.title() + " is located in: " + country.title() + ".")


describe_city('tampa')
describe_city('sao paolo', country='brazil')
describe_city('anchorage')
