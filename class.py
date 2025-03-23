"""
Python doesn't need explicit types (String, int, etc.).
No need for a separate main() method; execution starts at the top level."
"""

class Car:
    def __init__(self, brand, speed):  # Constructor
        self.brand = brand
        self.speed = speed

    def show_details(self):  # Method
        print(f"Brand: {self.brand}, Speed: {self.speed}")

# Creating an object
my_car = Car("Toyota", 120)
my_car.show_details()
