"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class User:

    def __init__(self,first_name, last_name, email):
        self.fn = first_name
        self.ln = last_name
        self.e = email

    def describe_user(self):
        print(f"The name user is {self.fn.title()} {self.ln.title()} and the email is {self.e}")

    def greet_user(self):
        print(f"Hi {self.fn}, nice to see you!")

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges")
        if self.privileges:
            for privilege in self.privileges:
                print(f" - {privilege}")
        else:
            print(f" -This user has no privileges.")


andrea = Admin('andrea', 'gomez', 'agomez@gmail.com')
andrea.describe_user()
andrea.privileges.show_privileges()

print("\n")
miguel = Admin('miguel', 'tenoch', 'mtecnoch@gmail.com' )
miguel.describe_user()

miguel_privileges = [
    'can reset password',
    'can delete account'
]
miguel.privileges.privileges = miguel_privileges
miguel.privileges.show_privileges()