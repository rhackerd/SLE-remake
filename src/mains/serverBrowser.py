import pygame
import sys
from mains.client import Client
from classes.logger import info, error
from pygame import quit
from mains.engine.game import Main_Engine

class ServerBrowser:
    def __init__(self, servers, screen, clock, config):
        self.servers = servers
        self.config = config
        self.server_frames = []
        self.clock = clock
        self.screen = screen
        self.create_server_list()
        self.scroll_offset = 0
        self.server_mouse = 0;
        self.main_game = None;

    def create_server_list(self):

        for i, server in enumerate(self.servers):
            frame = self.create_server_frame(server, i)
            self.server_frames.append((frame, server))

    def create_server_frame(self, server, i):
        return pygame.Rect(50, 50 + i * 100, 700, 90)

    def draw_server_name(self, frame, server):
        font = pygame.font.Font(None, 36)
        text = font.render(server["name"], True, (0, 0, 0))
        self.screen.blit(text, (60, -10 + frame.y))

    def draw_server_name_rect(self, frame, server):
        pygame.draw.rect(self.screen, (255, 255, 255), (59, 0 + frame.y, len(server["name"]) * 12, 4))

    def draw_server_motd(self, frame, server):
        font = pygame.font.Font(None, 21)
        text = font.render(server["motd"], True, (0, 0, 0))
        self.screen.blit(text, (60, 20 + frame.y))

    def draw_play_button(self, frame, server):
        font = pygame.font.Font(None, 36)
        text = font.render("Play", True, (0, 0, 0))
        self.screen.blit(text, (650, 30 + frame.y))

    def checkMotds(self):
        info("Checking motds...")
        for server in self.servers:
            info("checking " + server["name"] + " at " + server["ip"] + ":" + str(server["port"]))
            try:
                client = Client(server["ip"], server["port"], self.config)
                client.ping_server()
                server["motd"] = client.revc_raw_data().decode()
                server["name"] = client.revc_raw_data().decode()
            except ConnectionRefusedError:
                server["motd"] = "Unable to connect."
            except OSError:
                server["motd"] = "Os error could be firewall."

    def run(self):
        self.running = True
        self.checkMotds()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        self.scroll_offset -= 10
                    elif event.y < 0:
                        self.scroll_offset += 10
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.server_mouse = -1;
                        for frame, server in self.server_frames:
                            if frame.collidepoint(event.pos):
                                self.connect_to_server(server)
                                self.server_mouse = self.server_frames.index((frame, server))
                elif event.type == pygame.MOUSEMOTION:
                    self.server_mouse = -1;
                    for frame, server in self.server_frames:
                        if frame.collidepoint(event.pos):
                            self.server_mouse = self.server_frames.index((frame, server))




            self.screen.fill((255, 255, 255))
            if self.scroll_offset < 0:
                self.scroll_offset = 0
            for i, (frame, server) in enumerate(self.server_frames):
                frame.y = 50 + (i * 100) - self.scroll_offset
                if self.server_mouse == i:
                    pygame.draw.rect(self.screen, (255, 255, 255), frame, 0, 10)
                    pygame.draw.rect(self.screen, (100, 100, 100), frame, 4, 10)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), frame, 0, 10)
                    pygame.draw.rect(self.screen, (0, 0, 0), frame, 2, 10)
                self.draw_server_name_rect(frame, server)
                self.draw_server_name(frame, server)
                self.draw_server_motd(frame, server)
                self.draw_play_button(frame, server)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def connect_to_server(self, server):
        quit()
        self.main_game = Main_Engine(self.config, server)