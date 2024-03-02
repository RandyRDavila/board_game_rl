from setuptools import setup, find_packages

setup(
    name='board_game_rl',
    version='0.1.0',
    author='Randy R. Davila, Ph.D.',
    author_email='randyrdavila@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tabulate',
    ],
    description='A reinforcement learning package for board games',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RandyRDavila/board_game_rl',
)