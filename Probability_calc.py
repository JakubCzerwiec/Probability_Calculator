import copy
import random

class Hat() :
    def __init__(self, **balls) :
        self.balls = balls

        self.contents = []
        for ball, numbers in self.balls.items() :
            self.contents.extend(ball for i in range(numbers))

#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
hat = Hat(red=3, green=4)
print(hat.balls)
print(hat.contents)