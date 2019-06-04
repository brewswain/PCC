from user import User


class Privileges():
    """Represent the privileges that the administrator class has."""

    def __init__(self, privileges=[]):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Summarizes the privileges that an admin account contains."""
        print("You have access to the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege.capitalize())


class Admin(User):
    """Represent an administrator class of user."""

    def __init__(self, first_name, last_name, email, username='admin'):
        """Initialise attributes of the parent class."""
        super().__init__(first_name, last_name, username, email, )
        self.privileges = Privileges()


