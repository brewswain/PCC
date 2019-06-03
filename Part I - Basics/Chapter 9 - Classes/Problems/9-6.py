class Restaurant():
    """An attempt to model a restaurant."""

    def __init__(self,  restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Summarise the restaurant."""
        print("Welcome to " + self.restaurant_name +
              ", the Mecca of " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Display that the restaurant is open."""
        print("We're pleased to announce that we're open and ready for business!")

    def set_number_served(self, customers):
        """Lets you set number of customers served."""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("Sorry, you can't reduce the amount of customers served.")

    def increment_number_served(self, extra_served):
        """Add the given amount to the customer's served record."""
        self.number_served += extra_served


class IceCreamStand(Restaurant):
    """Represent aspects of food service exclusive to ice-cream stands."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """Initialise attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Here are the flavors that we have available!")
        for flavor in self.flavors:
            print("- " + flavor.title())


double_scooped = IceCreamStand('Double Scooped')
double_scooped.flavors = ['vanilla', 'chocolate', 'strawberry', 'praline']


double_scooped.describe_restaurant()
double_scooped.display_flavors()
