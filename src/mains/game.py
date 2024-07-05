import pygame
import sys

from mains.menu import Menu
from mains.serverBrowser import ServerBrowser
servers = [ {"name": "Default localhost", "ip": "127.0.0.1", "port": 25565, "motd": "Unable to get motd."}]

class Game:
    def __init__(self, debug, config):
        pygame.init()
        self.config = config
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.debug = debug
        self.menu = Menu(self.screen, self.clock)

    def run(self):
        while True:
            result = self.menu.run()
            if result == "play":
                self.server_browser = ServerBrowser(servers, self.screen, self.clock, self.config)
                self.server_browser.run()
            elif result == "quit":
                pygame.quit()
                sys.exit(0)

    def update(self):
        pass