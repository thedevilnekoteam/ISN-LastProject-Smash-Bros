# -*- coding: utf-8 -*-
import pygame

pygame.init()

fenetre = pygame.display.set_mode((600,600))
pygame.display.set_caption("Space Invader Mathis Charretier Ts01")

imageAlien = pygame.image.load("alien.png")
imageAlien = pygame.transform.scale(imageAlien, (30, 30))
imageVaisseau = pygame.image.load("vaisseau.png")
imageVaisseau = pygame.transform.scale(imageVaisseau, (60, 60))

arial20 = pygame.font.SysFont("arial", 20, False)

positionVaisseau = (300, 525)
positionAlien = (300, 10)
projectile = (-1, -1)
nbprojectile = 100
score = 0

BarreDeScore = arial20.render("score:" + str(score), True, pygame.Color(0, 255, 255))
BarreProjectile = arial20.render("projectile:" + str(nbprojectile), True, pygame.Color(0, 255, 255))


def dessiner():
    global imageAlien, imageVaisseau, fenetre, projectile
    fenetre.fill((0, 0, 0))
    fenetre.blit(imageVaisseau, positionVaisseau)
    fenetre.blit(imageAlien, positionAlien)
    fenetre.blit(BarreDeScore, (10, 30))
    fenetre.blit(BarreProjectile, (10, 10))
    if projectile != (-1, -1):
        pygame.draw.circle(fenetre, (255, 255, 255), projectile, 5)
    pygame.display.flip()

def gererClavierEtSouris():
    global continuer, positionVaisseau, projectile
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == True:
        projectile = (positionVaisseau[0] + 30, positionVaisseau[1])

    if touchesPressees[pygame.K_RIGHT] == True:
        if positionVaisseau[0] < 536:
            positionVaisseau = (positionVaisseau[0] + 5, positionVaisseau[1])
        else:
            positionVaisseau = (positionVaisseau[0], positionVaisseau[1])

    if touchesPressees[pygame.K_LEFT] == True:
        if positionVaisseau[0] > 0:
            positionVaisseau = (positionVaisseau[0] - 5, positionVaisseau[1])
        else:
            positionVaisseau = (positionVaisseau[0], positionVaisseau[1])

clock = pygame.time.Clock()
continuer = 1

while continuer == 1:
    clock.tick(60)
    dessiner()
    gererClavierEtSouris()

#point de disparition!
    if nbprojectile > 0:
        if projectile[1] <= 5 or positionAlien[0] - 35 < projectile[0] < positionAlien[0] + 35 and projectile[1] < positionAlien[1] + 35:
            projectile = (-1, -1)
        else:
            projectile = (projectile[0], projectile[1] - 5)

#Gestion du score et du !
    if positionAlien[0] - 35 < projectile[0] < positionAlien[0] + 35 and projectile[1] < positionAlien[1] + 35:
        score = score + 100
        BarreDeScore = arial20.render("score:" + str(score), True, pygame.Color(0, 255, 255))

#Gestion du nombre de projectile:
    if projectile == (330,515):
        if nbprojectile > 0:
            nbprojectile = nbprojectile - 1
            BarreProjectile = arial20.render("projectile:" + str(nbprojectile), True, pygame.Color(0, 255, 255))

pygame.quit()
