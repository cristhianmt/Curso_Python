"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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
        self.privileges = []
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"Can add a post  - {privilege}")


andrea = Admin('andrea', 'gomez', 'agomez@gmail.com')
andrea.privileges = ['can add post']
andrea.describe_user()
andrea.show_privileges()

print("\n")
miguel = Admin('miguel', 'tenoch', 'mtecnoch@gmail.com' )
miguel.privileges = ['can reset passwords']
miguel.describe_user()
miguel.show_privileges()