class User:
    """Create a user profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialise the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print("\nThis is " + self.first_name + " " +
              self.last_name + "'s user details:")
        print("Username: " + self.username)
        print("Email: " + self.email)

    def greet_user(self):
        """Print a greeting to the user."""
        print("\nWelcome, " + self.username + "!")

    def increment_login_attempts(self, logins):
        """
        Increment a total of login attempts made by the user.
        Simulate the user failing to login.
        """
        self.login_attempts += logins
        print("Login attempt " + str(self.login_attempts) + ".")
        if self.login_attempts >= 5:
            print(self.first_name + ", you've attempted to login " +
                  str(self.login_attempts) + " times. Would you like to reset your password?")

    def reset_login_attempts(self):
        """Reset the login attempts tally made."""
        print("\nResetting total login attempts.")
        self.login_attempts = 0


bob = User('bob', 'bobbieson', 'big bob', 'bobbingalong@bobmail.com')
bob.increment_login_attempts(5)
bob.reset_login_attempts()
print(bob.login_attempts)

# bob.describe_user()
# bob.greet_user()


# steve = User('steve', 'stevenson', 'small steve', 'sssssteve@stevenson.edu')
# steve.describe_user()
# steve.greet_user()
