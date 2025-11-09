# static attributes

# A static attribute (aka class attribute) is an attribute that
# belongs to the class itself, not to any specific instance of the class

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print("Username: {self.username}, Email: {self.email}")

user1 = User("dantheman", "dan@gmail.com")
user2 = User("sally123", "sally@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)