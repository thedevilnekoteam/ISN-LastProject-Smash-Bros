# Créé par charretm, le 16/02/2018 en Python 3.2
import pygame
from pygame.locals import *
from sys import exit
import time
import random
import notreprojetclass

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1000, 600), FULLSCREEN)
MenuPrincipal = pygame.image.load("Image Menu avec boutton v5.png").convert()

pygame.mixer.music.load("MusiqueMenu.mp3")
pygame.mixer.music.play()

def Quitter_Le_Jeu():
    global continuer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    Press = pygame.key.get_pressed()
    if Press[pygame.K_ESCAPE] == True:
        continuer = 0


def game_intro():

    wight = (255,255,255)
    green = (0,200,0)
    blue = (0,0,255)


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    #print(mouse)

    if 380+120 > mouse[0] > 380 and 290+60 > mouse[1] > 290:        #BOUTTON PLAY
        pygame.draw.rect(fenetre, blue,(380,290,120,60,), 2)

    else:
        pygame.draw.rect(fenetre, wight, (380,290,120,60,), 2)

    if 310+250 > mouse[0] > 310 and 385+60 > mouse[1] > 385:        #BOUTTON CREDITS
        pygame.draw.rect(fenetre, blue,(310,385,250,60), 2)
    else:
        pygame.draw.rect(fenetre, wight, (310,385,250,60), 2)

    if 335+200 > mouse[0] > 335 and 490+60 > mouse[1] > 490:        #BOUTTON COMMANDES
        pygame.draw.rect(fenetre, blue,(335,490,200,60), 2)
    else:
        pygame.draw.rect(fenetre, wight, (335,490,200,60), 2)



    pygame.display.update()
    clock.tick(120)


fenetre.blit(MenuPrincipal, (0,0))


#Rafraîchissement de l'écran
pygame.display.flip()

#Boucle infinie
clock = pygame.time.Clock()
continuer = 1

while continuer == 1:
    clock.tick(60)
    game_intro()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 380+120 > mouse[0] > 380 and 290+60 > mouse[1] > 290:
        notreprojetclass.run()
    Quitter_Le_Jeu()

pygame.quit()
exit()