# If you want to make the attributes private use "__"
# Name Mangling

class User:
    
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def clean_email(self):
        return self.__email.lower().strip()