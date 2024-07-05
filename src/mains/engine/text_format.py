# this is just for formatting text, and ursina has it's own default formatting but I want to keep it consistent with the rest of the game
# not for console this is for the game !

from ursina import color
from classes.kons_format import consoleFormat
from classes.logger import info, error
import re

class textFormat():
    def __init__(self, text):
        self.text = text
        self.print_list = ""


    def format(self):
        self.print_list = ""
        return consoleFormat(self.text).format()