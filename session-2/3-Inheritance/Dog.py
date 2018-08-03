from Pet import Pet

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'dog'
        print('becomes a ' + self.type)

    def woof(self):
        print('woof')

# only do this if we are running Dog.py in isolation
if __name__ == "__main__":
    dog = Dog('Diesel') # I might be bias but this is the best dog name
    dog.eat()
    dog.woof()

# TODO: Activity - Now create a cat with some extra behaviours
