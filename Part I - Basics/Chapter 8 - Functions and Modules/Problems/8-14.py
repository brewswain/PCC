def car_records(car_manufacturer, car_model, **extra_info):
    """Store information about a car in a dictionary."""
    car_index = {}

    car_index['manufacturer'] = car_manufacturer
    car_index['model'] = car_model

    for key, value in extra_info.items():
        car_index[key] = value
    return car_index


car_info = car_records('honda', 'civic', color='white', disc_brakes=True)
print(car_info)
