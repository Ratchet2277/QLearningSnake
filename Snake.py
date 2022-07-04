from copy import copy

from Coordinates import Coordinates
from Direction import Direction


class Snake:
    def __init__(self, position: Coordinates, direction: Direction = Direction.NORTH, length: int = 4):
        self.length = length
        self.direction = direction
        self.body: list[Coordinates] = []

        self.body.append(position)

        for i in range(0, length - 1):
            self.body.append(self.get_next_coordinate(-direction, i))

    def get_next_coordinate(self, direction: Direction = None, origin: int = 0) -> Coordinates:
        body_range = range(0, len(self.body))
        if origin not in body_range:
            origin = 0
        next_case = copy(self.body[origin])
        if not direction:
            direction = self.direction

        match direction:
            case Direction.NORTH:
                next_case.y -= 1
            case Direction.SOUTH:
                next_case.y += 1
            case Direction.EAST:
                next_case.x += 1
            case Direction.WEST:
                next_case.x -= 1
        return next_case

    def move(self) -> None:
        next_position = self.get_next_coordinate()
        self.body = [next_position] + self.body[0:self.length - 2]

    def turn(self, direction: Direction) -> None:
        if direction == -self.direction:
            return
        self.direction = direction

    def growth(self, step: int = 1):
        self.length += step

    def get_head_pos(self) -> Coordinates:
        return self.body[0]