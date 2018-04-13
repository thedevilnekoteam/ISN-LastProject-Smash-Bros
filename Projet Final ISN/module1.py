# Créé par charretm, le 16/02/2018 en Python 3.2
import pygame
from pygame.locals import *
from sys import exit
import time
import random

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((650, 720), FULLSCREEN)
MenuPrincipal = pygame.image.load("MenuPrincipal.png").convert()

pygame.mixer.music.load("MusiqueMenu.mp3")
pygame.mixer.music.play()

def dessiner():
    pygame.draw.rect(fenetre, (255, 255, 255), (275,330,100,60), 2)
    pygame.draw.rect(fenetre, (255, 255, 255), (262,440,125,60), 2)
    pygame.draw.rect(fenetre, (255, 255, 255), (225,550,200,60), 2)
    pygame.display.flip()


def GestionDuClick():
    global continuer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    Press = pygame.key.get_pressed()
    if Press[pygame.K_ESCAPE] == True:
        continuer = 0



fenetre.blit(MenuPrincipal, (0,0))


#Rafraîchissement de l'écran
pygame.display.flip()

#Boucle infinie
clock = pygame.time.Clock()
continuer = 1

while continuer == 1:
    clock.tick(60)
    dessiner()
    GestionDuClick()

pygame.quit()
exit()
