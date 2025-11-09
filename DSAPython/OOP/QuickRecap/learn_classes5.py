class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username} it's {self.username}")

user1 = User("dantheman", "dan@abc.com", "123")
user2 = User("batman", "bat@abc.com", "abc")

user1.say_hi_to_user(user2)

print(user1.email)
user1.email = "danny@123.com"
print(user1.email)