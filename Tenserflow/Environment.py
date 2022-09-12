from abc import ABC
from copy import copy

import numpy as np
import ts as ts
from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts

from Enum.Direction import Direction, Axis
from Enum.Obstruction import Obstruction
from Game.Board import Board


def create_board(size: int = 100) -> Board:
    return Board(size, size)


class SnakeEnvironment(py_environment.PyEnvironment, ABC):
    default_size: int = 100

    def __init__(self):
        super(SnakeEnvironment, self).__init__()
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
        result = []
        for direction in Direction:
            result.append(self._observe_one_direction(direction))
        return np.array(result, dtype=np.int32)

    def _observe_one_direction(self, direction: Direction):
        head = self.board.snake.get_head_pos()
        if direction in [Direction.NORTH, Direction.SOUTH]:
            axis = Axis.Y
        else:
            axis = Axis.X

        if direction > 0:
            delta = 1
        else:
            delta = -1

        distance = 0

        obstruction_type = Obstruction.WALL

        coordinate = copy(head)

        for i in range(0, self.default_size):
            distance += 1

            coordinate.increment_axis(axis, delta)

            if coordinate in self.board.snake.body:
                obstruction_type = Obstruction.SNAKE
                break
            if coordinate == self.board.goal:
                obstruction_type = Obstruction.GOAL
                break

        return [distance, obstruction_type]

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
            return ts.transition(np.array(self._state, dtype=np.int32), reward=reward, discount=1.0)
        else:
            self.episode_ended = True
            return ts.termination(np.array(self._state, dtype=np.int32),
                                  reward=len(self.board.snake.body) - (self.default_size ^ 2))
