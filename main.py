# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

from Game.Board import Board


def main_game():
    board = Board(100, 100)
    while board.on_going:
        board.run()
        board.draw()


if __name__ == '__main__':
    main_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
