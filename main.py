import pygame
from display import Display

FPS = 60
pygame.init()

frametimer = pygame.time.Clock()
WINDOW_WIDTH=1000
WINDOW_HEIGHT = 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display = Display()

playing = True
while playing:
    listen_events = pygame.event.get()
    for event in listen_events:
        if event.type == pygame.QUIT:
            playing = False

    display.update(listen_events)

    pygame.display.update()
    frametimer.tick(FPS)
pygame.quit()

