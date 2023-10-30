import pygame


class Window:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
