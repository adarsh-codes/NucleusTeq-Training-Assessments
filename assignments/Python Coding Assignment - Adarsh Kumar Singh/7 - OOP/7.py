class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal Base class"

    def display(self):
        print(f"{self.name} says {self.speak()}")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animal = Animal("Kangaroo")
print(animal.speak())
doggy = Dog("Bruno")
print(doggy.speak())