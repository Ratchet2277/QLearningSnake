# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from Coordinates import Coordinates
from Snake import Snake

if __name__ == '__main__':
    snake = Snake(Coordinates(10, 10))
    while True:
        snake.move()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
