# Getting and Setting data on objects
# Accessing and modifying data
# The traditional way: make the data private and use getters and setters
# To make attribute protected add "underscore" "_" - Example: "_email"

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email
    
user1 = User("dantheman", "dan@gmail.com", "123")
print(user1._email)