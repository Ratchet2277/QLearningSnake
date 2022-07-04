# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from Board import Board
from Coordinates import Coordinates
from Snake import Snake


def main_game():
    board = Board(100, 100)
    snake = Snake(Coordinates(10, 10))
    board.new_goal()
    board.add_snake(snake)
    while board.on_going:
        board.run()


if __name__ == '__main__':
    main_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
