# Créé par charretm, le 16/02/2018 en Python 3.2
import pygame
from pygame.locals import *
from sys import exit
import time
import random
# Initialisation de la bibliothèque Pygame
pygame.init()

# Création de la fenêtre
fenetre = pygame.display.set_mode((1000, 600))
MenuPrincipal = pygame.image.load(
    "Menu_Images/Image Menu v5.png").convert()

pygame.mixer.music.load("Menu_Musique/Musique.mp3")
pygame.mixer.music.play()


fenetre.blit(MenuPrincipal, (0, 0))
# Rafraîchissement de l'écran
pygame.display.flip()
# Boucle infinie
clock = pygame.time.Clock()
continuer = 1
while continuer == 1:
    clock.tick(60)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    Play = pygame.image.load(
        "Menu_Images/Button_48.png")  # On choisi le bouton
    posPlay = (390, 290)  # On donne une position
    fenetre.blit(Play, posPlay)  # On l'affiche sur la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and posPlay[0] + 137 > mouse[0] > posPlay[0] and posPlay[1] + 143 > mouse[1] > posPlay[1]:
            print("ca marche!")

        # if 310 + 250 > mouse[0] > 310 and 385 + 60 > mouse[1] > 385:  # BOUTTON CREDITS

        #    if 335 + 200 > mouse[0] > 335 and 490 + 60 > mouse[1] > 490:  # BOUTTON COMMANDES

    pygame.display.update()
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    Press = pygame.key.get_pressed()
    if Press[pygame.K_ESCAPE] == True:
        continuer = 0

pygame.quit()
exit()
