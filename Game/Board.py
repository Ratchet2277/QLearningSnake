import random
import threading

import pygame

from Game.Drawer import Drawer
from Game.Interface.BoardInterface import BoardInterface
from Struct.Coordinates import Coordinates
from .Interface.InputInterface import InputInterface
from .KeyboardInput import KeyboardInput
from .Snake import Snake


class Board(BoardInterface):

    def __init__(self, height: int, width: int, input: InputInterface = None):
        super().__init__(height, width, input)
        self.free_cell = []
        self.height = height
        self.width = width
        self.snake = None
        self.goal = None
        self.on_going = True
        self.snake = Snake(Coordinates(width >> 1, height >> 1))
        if not input:
            input = KeyboardInput()
        self.snake.set_input(input)
        self.new_goal()
        self.drawer = Drawer(self)

    def get_height(self) -> int:
        return self.height

    def get_width(self) -> int:
        return self.width

    def get_snake(self) -> Snake:
        return self.snake

    def get_goal(self) -> Coordinates:
        return self.goal

    def process_events(self) -> None:
        if pygame.event.peek(pygame.QUIT):
            self.on_going = False
            self.snake.is_alive = False
            self.drawer.draw()
            pygame.time.wait(1000)
            pygame.quit()
            exit()

    def add_goal(self, goal: Coordinates):
        self.goal = goal

    def game_over(self):
        self.on_going = False
        self.snake.is_alive = False
        self.drawer.draw()
        pygame.time.wait(1000)
        pygame.quit()
        exit()

    def run(self) -> None:
        pygame.event.pump()
        if self.snake.check_tail_collision():
            self.game_over()
        if not self.snake.is_alive:
            self.game_over()
        self.process_events()
        self.snake.move()
        if not 0 < self.snake.get_head_pos().x <= self.width:
            self.game_over()
        if not 0 < self.snake.get_head_pos().y <= self.height:
            self.game_over()
        if self.snake.get_head_pos() == self.goal:
            self.snake.grow()
            self.new_goal()

    def new_goal(self):
        self.get_all_empty_cell()
        if not len(self.free_cell):
            self.game_over()
            return
        self.goal = random.choice(self.free_cell)

    def get_all_empty_cell(self) -> None:
        self.free_cell = []
        threads = []
        for x in range(0, self.height):
            thread = threading.Thread(target=self.get_empty_cell_in_row, args=(x,))
            thread.start()
            print(thread)
            threads.append(thread)

        for thread in threads:
            print(thread)
            thread.join()

    def get_empty_cell_in_row(self, row: int) -> None:
        for x in range(0, self.width):
            cell = Coordinates(x, row)
            if cell not in self.snake.body:
                self.free_cell.append(cell)
