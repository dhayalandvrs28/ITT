class Fan:
    def __init__(self, speed="Medium"):
        self.speed = speed

    def status(self):
        print(f"The fan speed is {self.speed}")

# Usage
fan1 = Fan()          # Uses default
fan1.status()
fan2 = Fan("High")    # Overrides default
fan2.status()