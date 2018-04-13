import pygame
from pygame.locals import *
from sys import exit
pygame.init()

fenetre = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
pygame.display.set_caption("Brawl")

def gererClavierEtSouris():
    global continuer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

        Press = pygame.key.get_pressed()
        if Press[pygame.K_ESCAPE] == True:
            continuer = 0


clock = pygame.time.Clock()
continuer = 1

while continuer == 1:
    clock.tick(60)
    gererClavierEtSouris()

pygame.quit()
exit()