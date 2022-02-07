import pygame
from pygame.locals import *
from Object import *

pygame.init()

pygame.display.set_caption("Testfenster")
screen = pygame.display.set_mode((500, 500), RESIZABLE)
clock = pygame.time.Clock()

screen.fill((255, 255, 255))

mars = Object(2000, (200, 400), 20)

run = True
while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(mars.image, mars.get_pos())
    pygame.display.update()
    clock.tick(30)
