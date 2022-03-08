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


class Admin(User):
    """Represent an administrator class of user."""

    def __init__(self, first_name, last_name, email, username='admin'):
        """Initialise attributes of the parent class."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Summarizes the privileges that an admin account contains."""
        print("Welcome, " + self.username +
              ". You have access to the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege.capitalize())


my_admin = Admin('brandon', 'lee', 'blee@admin.com')
my_admin.describe_user()


my_admin.show_privileges()
