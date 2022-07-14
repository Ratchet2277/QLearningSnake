import numpy as np
import ts as ts
from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts

from Enum.Direction import Direction
from Enum.Obstruction import Obstruction
from Game.Board import Board
from Struct.Coordinates import Coordinates


def create_board(size: int = 100) -> Board:
    return Board(size, size)


class SnakeEnvironement(py_environment.PyEnvironment):
    default_size: int = 100

    def __init__(self):
        super(SnakeEnvironement, self).__init__()
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=-2, maximum=2, name='snake direction')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(4, 2,), dtype=np.int32, minimum=0, maximum=[self.default_size, 3], name='observation')
        self.board = create_board(self.default_size)
        self.initial_size = len(self.board.snake.body)
        self._state = self._observation()
        self.episode_ended = False

    def observation_spec(self):
        return self._observation_spec

    def action_spec(self):
        return self._action_spec

    def _observation(self):
        result = [self._observe_one_direction(Direction.NORTH), self._observe_one_direction(Direction.SOUTH),
                  self._observe_one_direction(Direction.EAST), self._observe_one_direction(Direction.WEST)]
        return np.array(result, dtype=np.int32)

    def _observe_one_direction(self, direction: Direction):
        head = self.board.snake.get_head_pos()
        if direction in [Direction.NORTH, Direction.SOUTH]:
            axis = 1
        else:
            axis = 0

        if direction > 0:
            delta = 1
        else:
            delta = -1

        distance = 0

        if axis:
            variable_coordinate = head.x
        else:
            variable_coordinate = head.y

        type = Obstruction.WALL

        while variable_coordinate in range(0, self.default_size):
            distance += 1
            variable_coordinate += delta

            if axis:
                coordinate = Coordinates(variable_coordinate, head.y)
            else:
                coordinate = Coordinates(head.x, variable_coordinate)

            if coordinate in self.board.snake.body:
                type = Obstruction.SNAKE
                break
            elif coordinate == self.board.goal:
                type = Obstruction.GOAL
                break

        return [distance, type]

    def _reset(self):
        self.board = create_board(self.default_size)
        self.episode_ended = False
        self._state = self._observation()
        return ts.restart(self._state)

    def _step(self, action):
        if self.episode_ended:
            return self._reset()

        self.board.run(action)
        self._state = self._observation()

        if self.board.on_going:
            reward = 0
            if (len(self.board.snake.body) - self.initial_size) > 0:
                reward = 1
            return ts.transition(np.array([self._state], dtype=np.int32), reward=reward, discount=1.0)
        else:
            self.episode_ended = True
            return ts.termination(np.array([self._state], dtype=np.int32),
                                  reward=len(self.board.snake.body) - (self.default_size ^ 2))
