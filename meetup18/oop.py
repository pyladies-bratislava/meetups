"""Object Oriented Programming with python"""


class Dog:
    """Class that represents an animal of the type dog."""
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False


class BullDog(Dog):
    """Subclass of Dog that represents the Bulldog species"""


# Functions to interact with the dogs
def feed_dogs(dogs):
    for dog in dogs:
        print('I am feeding {name}.'.format(name=dog.name))
        dog.eat()


def are_dogs_hungry(dogs):
    # List of booleans that contain the is_hungry attribute of each dog
    hungry_dogs = [dog.is_hungry for dog in dogs]

    if all(hungry_dogs):
        print('All my dogs are hungry.')
    elif any(hungry_dogs):
        print('Some of my dogs are hungry.')
    else:
        print('My dogs are not hungry.')
