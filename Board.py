import random

from Coordinates import Coordinates
from Snake import Snake


class Board:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.snake = None
        self.goal = None
        self.on_going = True
        self.snake = Snake(Coordinates(width >> 1, height >> 1))
        self.new_goal()

    def add_goal(self, goal: Coordinates):
        self.goal = goal

    def run(self) -> None:
        if not self.snake.is_alive:
            self.on_going = False
            return
        self.snake.move()
        if not 0 < self.snake.get_head_pos().x <= self.width:
            self.snake.is_alive = False
            self.on_going = False
            return
        if not 0 < self.snake.get_head_pos().y <= self.height:
            self.snake.is_alive = False
            self.on_going = False
            return
        if self.snake.get_head_pos() != self.goal:
            return
        self.snake.growth()

    def new_goal(self):
        free_cell = self.get_all_empty_cell()
        if not len(free_cell):
            self.on_going = False
            return
        self.goal = random.choice(free_cell)

    def get_all_empty_cell(self) -> list[Coordinates]:
        free_cell = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = Coordinates(x, y)
                if cell not in self.snake.body:
                    free_cell.append(cell)
        return free_cell
