import pygame

from Game.Interface.BoardInterface import BoardInterface
from Game.Interface.DrawerInterface import DrawerInterface


class Drawer(DrawerInterface):
    def __init__(self, bord: BoardInterface, frame_rate: int = 0, square_size: int = 8):
        self.bord = bord
        self.frame_rate = frame_rate
        self.square_size = square_size
        pygame.init()
        pygame.display.set_caption('Snake')
        self.screen = pygame.display.set_mode(
            (bord.get_height() * self.square_size, bord.get_height() * self.square_size))
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for cell in self.bord.get_snake().body:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (cell.x * self.square_size, cell.y * self.square_size, self.square_size,
                              self.square_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (
            self.bord.get_goal().x * self.square_size, self.bord.get_goal().y * self.square_size, self.square_size,
            self.square_size))
        pygame.display.flip()
        self.clock.tick(self.frame_rate)
