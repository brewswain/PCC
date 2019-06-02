class User:
    """Create a user profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialise the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print("\nThis is " + self.first_name + " " +
              self.last_name + "'s user details:")
        print("Username: " + self.username)
        print("Email: " + self.email)

    def greet_user(self):
        """Print a greeting to the user."""
        print("\nWelcome, " + self.username + "!")


bob = User('bob', 'bobbieson', 'big bob', 'bobbingalong@bobmail.com')
bob.describe_user()
bob.greet_user()


steve = User('steve', 'stevenson', 'small steve', 'sssssteve@stevenson.edu')
steve.describe_user()
steve.greet_user()
