class Animal:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def speak(self):
        return "i speak"


class Dog(Animal):
    def __init__(self, name, age, breed):
        print("From Dog")
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        super().speak()
        return "Dog speak"



class Cat(Animal):
    pass


dog = Dog("Bingo", 10, "local")
print(Dog.speak(dog))
print(dog.name)
print(dog.breed)
print(Animal.speak(dog))
print(dog.speak())

