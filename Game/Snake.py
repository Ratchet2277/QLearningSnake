from copy import copy

from Game.Interface.InputInterface import InputInterface
from Struct.Coordinates import Coordinates
from Enum.Direction import Direction


class Snake:
    def __init__(self, position: Coordinates, direction: Direction = Direction.NORTH, length: int = 4):
        self.length = length
        self.direction = direction
        self.body: list[Coordinates] = []
        self.is_alive = True
        self.input = None
        self.body.append(position)

        for i in range(0, length - 1):
            self.body.append(self.get_next_coordinate(-direction, i))

    def set_input(self, input: InputInterface):
        self.input = input

    def get_next_coordinate(self, direction: Direction = None, origin: int = 0) -> Coordinates:
        body_range = range(0, len(self.body))
        if origin not in body_range:
            origin = 0
        next_cell = copy(self.body[origin])
        if not direction:
            direction = self.direction

        match direction:
            case Direction.NORTH:
                next_cell.y -= 1
            case Direction.SOUTH:
                next_cell.y += 1
            case Direction.EAST:
                next_cell.x += 1
            case Direction.WEST:
                next_cell.x -= 1
        return next_cell

    def move(self) -> None:
        if not self.input:
            raise Exception("No input set")

        input = self.input.get_input()
        if input:
            self.turn(input)

        if not self.is_alive:
            return
        self.body = [self.get_next_coordinate()] + self.body[0:self.length - 2]

    def turn(self, direction: Direction) -> None:
        if abs(direction) == abs(self.direction):
            return
        self.direction = direction

    def grow(self, step: int = 1):
        self.length += step

    def get_head_pos(self) -> Coordinates:
        return self.body[0]

    def check_tail_collision(self) -> bool:
        if self.get_head_pos() in self.body[1:]:
            self.is_alive = False
            return True
        return False
