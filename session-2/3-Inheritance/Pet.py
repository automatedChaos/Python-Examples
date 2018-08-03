class Pet(object):

    def __init__(self, name):
        print('What started as a pet...')
        self.type = 'generic'
        self.posX = 0
        self.posY = 0
        self.name = name
        self.foodKg = 1
        self.sleep = 1
        self.exercise


    def eat(self):
        for x in range(self.foodKg):
            print('nom ')

    def sleep(self):
        for x in range(self.sleep):
            print('z ')

    def exercise(self):
        dist += self.exercise * self.speed
        self.xPos+= dist
        print(self.name + ' has travelled ' + dist + ' mile')

# only do this if we are running Dog.py in isolation
if __name__ == "__main__":
    pet = Pet('Diesel') # I might be bias but this is the best dog name
    pet.eat()
