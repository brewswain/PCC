class Restaurant():
    """An attempt to model a restaurant."""

    def __init__(self,  restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """Summarise the restaurant."""
        print("Welcome to " + self.restaurant_name +
              ", the Mecca of " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Display that the restaurant is open."""
        print("We're pleased to announce that we're open and ready for business!")


tabouli = Restaurant('papa ganoush', 'arabic')
tabouli.describe_restaurant()

faviken = Restaurant('faviken', 'swedish')
faviken.describe_restaurant()

noma = Restaurant('noma', 'danish')
noma.describe_restaurant()
