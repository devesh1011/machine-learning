# Base class (Parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

    def introduce(self):
        print(f"I am {self.name}, a {self.species}.")

# Derived class (Child class) inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def introduce(self):
        print(f"I am {self.name}, a {self.breed} dog.")

# Another derived class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def speak(self):
        return "Meow!"

    def introduce(self):
        print(f"I am {self.name}, a {self.breed} cat.")


def main():
    fido = Dog("Fido", "Golden Retriever")
    fluffy = Cat("Fluffy", "Siamese")

    fido.introduce()
    print(f"Fido says: {fido.speak()}")

    fluffy.introduce()
    print(f"Fluffy says: {fluffy.speak()}")

# Example usage:
if __name__ == "__main__":
    main()