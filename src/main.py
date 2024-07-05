import pygame
import sys
import argparse
from os import path
from mains.game import Game
from classes.config import Config
from classes.logger import info, error

def getConfig():
    return config

config = None

def main(arg):
    global game

    try:
        arg.config
        if path.isfile(arg.config):
            global config
            config = Config(arg.config)
        else:
            info(f"Couldn't find file {arg.config}")
            return sys.exit(-1)
    except:
        info("Config was not set please set it using --config or -c")
        return sys.exit(-1)

    pygame.init()

    game = Game(arg.debug, config)
    game.run()

    return sys.exit(0)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Game")
    parse.add_argument('--debug', '-d', action="store_true", help='Enable debugging')
    parse.add_argument('--config', "-c", help="Config that will be used to run the program")

    arg = parse.parse_args()
    main(arg)