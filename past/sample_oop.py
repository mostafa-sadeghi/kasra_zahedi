# class Car:
#     def __init__(self, name, year, color):
#         self.name = name
#         self.year = year
#         self.color = color

#     def move(self):
#         print(f'{self.name} is moving')


# car1 = Car("Benz", 2022, "white")
# car1.move()

# car2 = Car("Toyota",2023,"black")
# car2.move()


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def speak(self):
        print(f'{self.name} is speaking')

    def move(self):
        print(f'{self.name} is moving')
    
    def get_age(self):
        print(f'{self.name} has {self.age} years old')

p1 = Person("sara",22,170)
p1.speak()
p1.move()
p1.get_age()