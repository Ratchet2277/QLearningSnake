# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tf_agents.environments import utils

# Press the green button in the gutter to run the script.
from Tenserflow.Environment import SnakeEnvironement

if __name__ == '__main__':
    environment = SnakeEnvironement()
    utils.validate_py_environment(environment, episodes=5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
