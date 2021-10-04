import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 175), 30)
circle(screen, (255, 0, 0), (250,175), 20)
circle(screen, (0, 0, 0), (150,175), 15)
circle(screen, (0, 0, 0), (250,175), 15)
polygon(screen, (0, 0, 0), [(120, 90), (110,100), (200, 175), (210, 165)])
polygon(screen, (0, 0, 0), [(230,155), (235, 165), (285, 90), (280, 80)])
polygon(screen, (0, 0, 0), [(150,250), (150, 270), (250, 270), (250, 250)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
