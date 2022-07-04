from Coordinates import Coordinates
from Snake import Snake


class Board:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.snake = None
        self.goal = None

    def add_snake(self, snake: Snake):
        self.snake = snake

    def add_goal(self, goal: Coordinates):
        self.goal = goal
