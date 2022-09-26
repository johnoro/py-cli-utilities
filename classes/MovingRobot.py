# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import math

class MovingRobot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction, steps):
        if direction == "UP":
            self.y += steps
        elif direction == "DOWN":
            self.y -= steps
        elif direction == "LEFT":
            self.x -= steps
        elif direction == "RIGHT":
            self.x += steps

    def distance(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))

def main():
    movingRobot = MovingRobot()
    print(f'currently available commands: UP, DOWN, LEFT, RIGHT')
    while True:
        try:
            s = input("Enter a direction and steps: ")
            if not s:
                break
        except KeyboardInterrupt:
            break
        direction, steps = s.split(" ")
        movingRobot.move(direction, int(steps))
    print()
    print(f'Final distance: {movingRobot.distance()}')

if __name__ == "__main__":
    main()
