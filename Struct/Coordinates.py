from Enum.Direction import Axis


class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def increment_axis(self, axis: Axis, step: int = 1) -> None:
        match axis:
            case Axis.X:
                self.x += step
            case Axis.Y:
                self.y += step
            case _:
                raise Exception("Invalid axis")
