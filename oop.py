# Object Oriented Programming.

# OOP is a programming paradigm.

# With OOP concept of objects come into picture.

# An object can conatin data, code, data in the form of fields and code, and procedures.

# Procedures are nothing but methods inside a class. This example only validates for the 
# programming languaues that support class based OOP.

# Basic Terminologies.

# Class - A blueprint of the object.

# Objects- Variables, Function, etc, that deal with or act on data.

# Attributes- Data inside the class. Variables.

# Syntax of creating a class.


from hashlib import new
from types import new_class


class Example:

    # Self is a python reserved keyword.

    # Self helps you reuse the class with different objects.

    # You can use other word in place of self too.

    def __init__(self, name):
        self.your_name = name

    def welcome(self):
        print(f"Hello {self.your_name}, welcome to my function.")


# Below is how an object of a class is created.
example_class_object = Example("Kumar")

# Below shows how you access a particular method inside a class for your object.
example_class_object.welcome()

# More relatable example.

class Car:

    def __init__(self, fuel_type, engine_displacement, make, year ) -> None:
        self.fuel_type = fuel_type
        self.engine_displacement = engine_displacement
        self.make = make
        self.year = year

    def car_info(self):
        return f"Engine fuel type is {self.fuel_type}; displacement is {self.engine_displacement}; make is {self.make}, and year is {self.year}"

    def fuel_type_info(self, new_fuel_type):
        self.fuel_type = new_fuel_type

    def displacement_info(self, new_displacement):
        self.engine_displacement = new_displacement

    def make_and_year(self, new_make, new_year):
        self.make = new_make
        self.year = new_year

car_object = Car("Disel", 1.5, "Honda", 2018)

# Information before modification.
print("Old car info: ----", car_object.car_info())
print(car_object.fuel_type, car_object.make, car_object.engine_displacement, car_object.year)

# Information after modifying the data.

car_object.displacement_info(2.0)
car_object.fuel_type_info("Petrol")
car_object.make_and_year("Hyundai", 2021)

print("New car info: ----", car_object.car_info())

print(car_object.fuel_type, car_object.make, car_object.engine_displacement, car_object.year)


