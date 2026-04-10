class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal):
    def speak(self):
        print("Tweet")

# Usage
my_bird = Bird()
my_bird.speak()S