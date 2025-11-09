class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof woof")

dog1 = Dog("Bruce", "Scottish Terrier")
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Freya", "Greyhound")
dog2.bark()
print(dog2.name)
print(dog2.breed)