class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()

user1 = User("dantheman", " Dan@gmail.com ", "123")
print(user1.clean_email())        

# The "Consenting Adults" Philosophy