from importlib import util
import sys


def checkForPygame():
    if util.find_spec("ursina") == None:
        return False
    else:
        return True