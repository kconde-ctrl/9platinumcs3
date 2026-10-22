class Animal:

    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Lion(Animal):

    def make_sound(self):
        print(f"{self.name} roars loudly!")

    def eat(self):
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal):

    def make_sound(self):
        print(f"{self.name} trumpets!")

    def eat(self):
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal):

    def make_sound(self):
        print(f"{self.name} chatters!")

    def eat(self):
        print(f"{self.name} eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("-----")
