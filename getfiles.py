import pygame

WINDOW_WIDTH=1000
WINDOW_HEIGHT = 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Memory Game')
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Images(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.found = []
        self.name = filename.split('.')[0]

        self.origine_image = pygame.image.load('images/' + filename)

        self.back_image = pygame.image.load('images/' + filename)
        pygame.draw.rect(self.back_image, WHITE, self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft = (x, y))
        self.shown = False

    def update(self):
        self.image = self.origine_image if self.shown else self.back_image

    def show(self):
        self.shown = True
    def hide(self):
        self.shown = False
