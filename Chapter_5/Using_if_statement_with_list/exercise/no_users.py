"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message
is printed.
"""

# usernames = ['adrian', 'admin', 'carl', 'david', 'susie']
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some user!")
