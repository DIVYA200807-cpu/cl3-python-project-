class Robot:
    def __init__(self, name, color, purpose):
        self.name = name
        self.color = color
        self.purpose = purpose

    def introduce(self):
        print("----- Robot Introduction -----")
        print("Hello! My name is", self.name)
        print("My color is", self.color)
        print("My purpose is", self.purpose)
        print()



robot1 = Robot("Tom", "Blue", "Helping Students")
robot2 = Robot("Jerry", "Red", "Cleaning the House")


robot1.introduce()
robot2.introduce()