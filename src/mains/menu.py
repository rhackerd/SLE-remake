import pygame
import sys

class Menu:
    def __init__(self, screen, clock):
        self.active = True
        self.screen = screen
        self.clock = clock

        self.play_button = pygame.Rect(350, 250, 100, 50)
        self.settings_button = pygame.Rect(350, 320, 100, 50)
        self.quit_button = pygame.Rect(350, 390, 100, 50)

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), self.play_button, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.settings_button, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.quit_button, 2)

        font = pygame.font.Font(None, 36)
        text = font.render("Play", True, (0, 0, 0))
        self.screen.blit(text, (360, 255))
        text = font.render("Settings", True, (0, 0, 0))
        self.screen.blit(text, (360, 325))
        text = font.render("Quit", True, (0, 0, 0))
        self.screen.blit(text, (360, 395))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.collidepoint(event.pos):
                    return "play"
                elif self.settings_button.collidepoint(event.pos):
                    return "settings"
                elif self.quit_button.collidepoint(event.pos):
                    return "quit"
        return True

    def run(self):
        while True:
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
            result = self.handle_events()
            if result == "play":
                return "play"
            elif result == "quit":
                pygame.quit()
                sys.exit(0)