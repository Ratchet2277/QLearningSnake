import random
import pygame
from pygame.event import Event

from Coordinates import Coordinates
from Direction import Direction
from Snake import Snake


class Board:
    square_size = 8
    frame_rate = 30

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.snake = None
        self.goal = None
        self.on_going = True
        self.snake = Snake(Coordinates(width >> 1, height >> 1))
        self.new_goal()
        pygame.init()
        pygame.display.set_caption('Snake')
        self.screen = pygame.display.set_mode((height * self.square_size, width * self.square_size))
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for cell in self.snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (cell.x * self.square_size, cell.y * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (
            self.goal.x * self.square_size, self.goal.y * self.square_size, self.square_size, self.square_size))
        pygame.display.flip()

    def process_events(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.on_going = False
                self.snake.is_alive = False
                self.draw()
                pygame.time.wait(1000)
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.process_key(event)

    def process_key(self, event: Event) -> None:
        match event.key:
            case pygame.K_ESCAPE:
                self.on_going = False
                self.snake.is_alive = False
                self.draw()
                pygame.time.wait(1000)
                pygame.quit()
                exit()
            case pygame.K_UP:
                self.snake.turn(Direction.NORTH)
            case pygame.K_DOWN:
                self.snake.turn(Direction.SOUTH)
            case pygame.K_LEFT:
                self.snake.turn(Direction.WEST)
            case pygame.K_RIGHT:
                self.snake.turn(Direction.EAST)

    def add_goal(self, goal: Coordinates):
        self.goal = goal

    def game_over(self):
        self.on_going = False
        self.snake.is_alive = False
        self.draw()
        pygame.time.wait(1000)
        pygame.quit()
        exit()

    def run(self) -> None:
        self.clock.tick(self.frame_rate)
        if self.snake.check_tail_collision():
            self.game_over()
        if not self.snake.is_alive:
            self.game_over()
        self.process_events(pygame.event.get())
        self.snake.move()
        if not 0 < self.snake.get_head_pos().x <= self.width:
            self.game_over()
        if not 0 < self.snake.get_head_pos().y <= self.height:
            self.game_over()
        if self.snake.get_head_pos() == self.goal:
            self.snake.grow()
            self.new_goal()

    def new_goal(self):
        free_cell = self.get_all_empty_cell()
        if not len(free_cell):
            self.game_over()
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
