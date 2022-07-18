from distutils.core import setup

setup(name='QLearning Snake',
      version='1.0',
      description='A Basic Q-Learning Snake made for self-educational purposes',
      author='Jérémy Saudemont',
      author_email='jeremysaudemont@gmail.com',
      install_requires=[
          'tf_agents',
          'tensorflow',
          'pygame',
      ])
