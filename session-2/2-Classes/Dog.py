class Dog:
    legs = 4

    def __init__(self):
        print('A dog is born!')
        self.position = 0

    def woof(self):
        print('bark woof bark woof')

    def walk(self):
        self.position += 1
        print(self.position)

# only do this if we are running Dog.py in isolation
if __name__ == "__main__":
    dog1 = Dog()
    dog1.woof()

    for x in range(100):
        dog1.walk()
