# libraries
from Object import Object
import pygame
from pygame.locals import *
from calculations import *
import math

pygame.init()
print("started")

# Variablen/KONSTANTEN setzen
W, H = 1280, 720
FPS = 30
t = 1 / FPS
WEISS = (255, 255, 255)
BLACK = (0, 0, 0)

# define and open screen
screen = pygame.display.set_mode((W, H), RESIZABLE)
pygame.display.set_caption("Space Simulator")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

celestials = [Object(2000000000000, (500, 500), 30, ID=0, name="sun", v=0),
              Object(1000000000000, (510, 500), 20, ID=1, name="mars", v=0)
              ]

run = True
while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    for celest in celestials:

        celestials[0].calc_force(celestials[1])

    celestials[0].do_calculations(t)

    for celest in celestials:
        screen.blit(celest.image, celest.get_pos())

    pygame.display.update()
    clock.tick(FPS)
