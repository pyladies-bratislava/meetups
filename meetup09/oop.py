"""Object Oriented Programming with python"""


class Dog:
    """Class that represents an animal of the type dog."""
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def __str__(self):
        return "I am {name} the Dog and I am {age} years old.".format(name=self.name,
                                                                      age=self.age)

    def eat(self):
        self.is_hungry = False


class BullDog(Dog):
    """Subclass of Dog that represents the Bulldog species"""

    def __str__(self):
        return "I am {name} the bulldog and I am ugly.".format(name=self.name)


# Functions to interact with the dogs
def feed_dogs(*dogs):
    for dog in dogs:
        print('I am feeding {name}.'.format(name=dog.name))
        dog.eat()


def are_dogs_hungry(*dogs):
    # List of booleans that contain the is_hungry attribute of each dog
    hungry_dogs = [dog.is_hungry for dog in dogs]

    if all(hungry_dogs):
        print('All my dogs are hungry.')
    elif any(hungry_dogs):
        print('Some of my dogs are hungry.')
    else:
        print('My dogs are not hungry.')


def get_biggest_number(*args):
    number = max(args)
    print("The oldest dog is {} years old.".format(number))


def get_biggest_number2(*args):
    number = max(i.age for i in args)
    print("The oldest dog is {} years old.".format(number))


# Example of interaction with the classes and functions
# I have 4 dogs
bull = BullDog('bull', 12)
bobby = Dog('bobby', 10)
dunco = Dog('dunco', 3)
laika = Dog('laika', 6)
my_dogs = [bobby, bull, dunco, laika]

# Get a look at the __str__ method
print(bobby)
print(dunco)
print(laika)
print(bull)


# Let's check if the dogs are hungry
are_dogs_hungry(*my_dogs)
feed_dogs(bobby, bull, dunco)
are_dogs_hungry(*my_dogs)


# Let's get the oldest dog
get_biggest_number(bobby.age, dunco.age, laika.age)
get_biggest_number2(bobby, dunco, laika)
