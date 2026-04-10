
# =================================================================
# PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) EXAMPLES
# =================================================================

# 1. QUESTION: Create a simple class with a method to simulate driving.
class Car:
    def drive(self):
        print("Car: Vroom!")

# 2. QUESTION: Create a class with an __init__ constructor to store and display book details.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: '{self.title}' by {self.author}")

# 3. QUESTION: Create a Rectangle class that calculates area based on length and width.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# 4. QUESTION: Create a Fan class that uses a default argument in the constructor.
class Fan:
    def __init__(self, speed="Medium"):
        self.speed = speed

    def status(self):
        print(f"Fan: The fan is running at {self.speed} speed.")

# 5. QUESTION: Demonstrate Inheritance and Method Overriding using Animal and Bird.
class Animal:
    def speak(self):
        print("Animal: Animal speaks")

class Bird(Animal):
    def speak(self):
        print("Bird: Tweet Tweet!")

# 6. QUESTION: Define a simple Dog class with a bark method.
class Dog:
    def bark(self):
        print("Dog: Woof")

# 7. QUESTION: Create a Student class to store a name and age, then display them.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student: {self.name} is {self.age} years old.")

# =================================================================
# EXECUTION BLOCK (RUNNING THE EXAMPLES)
# =================================================================
if __name__ == "__main__":
    print("="*60)
    print("        PYTHON OOP EXAMPLES - EXECUTION RESULTS")
    print("="*60)

    # 1. Car Output
    print("\n[1] CLASS: Car (Basic Method)")
    my_car = Car()
    my_car.drive()

    # 2. Book Output
    print("\n[2] CLASS: Book (Constructor & Attributes)")
    my_book = Book("The Prestige", "Christopher Nolan")
    my_book.display()

    # 3. Rectangle Output
    print("\n[3] CLASS: Rectangle (Returning Values)")
    rect = Rectangle(10, 5)
    print(f"Action: area() -> Output: {rect.area()}")

    # 4. Fan Output
    print("\n[4] CLASS: Fan (Default vs Custom Arguments)")
    fan1 = Fan()          # Uses default
    fan1.status()
    fan2 = Fan("High")    # Overrides default
    fan2.status()

    # 5. Inheritance Output
    print("\n[5] CLASS: Bird (Inheriting from Animal)")
    my_bird = Bird()
    my_bird.speak()

    # 6. Dog Output
    print("\n[6] CLASS: Dog (No Constructor)")
    my_dog = Dog()
    my_dog.bark()

    # 7. Student Output
    print("\n[7] CLASS: Student (User Data Storage)")
    stu = Student("Abishek V H", 19)
    stu.display()

    print("\n" + "="*60)
    print("            END OF PROGRAM DEMONSTRATION")
    print("="*60)

