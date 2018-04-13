import pygame
import random
pygame.init()

fenetre = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Smash Mugging")
animD = [pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (1).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (2).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (3).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (4).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (5).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (6).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (7).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunD (8).png")]


animG = [pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (1).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (2).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (3).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (4).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (5).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (6).png"),
         pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (7).png"), pygame.image.load("LES SPRITES/png/LeRobot/Run/RunG (8).png")]

# nemarche toujours pas:
Feu = [pygame.image.load("LES SPRITES/png/LeRobot/Shoot/Bullet_001.png"),
       pygame.image.load("LES SPRITES/png/LeRobot/Shoot/Bullet_002.png")]  #AUGMENTER LA TAILLE DES BOULES ?


animDr = [pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__000.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__001.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__002.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__003.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__004.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__005.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__006.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__007.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__008.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaD/Run__009.png")]


animGa = [pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__000.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__001.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__002.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__003.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__004.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__005.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__006.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__007.png"),
          pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__008.png"), pygame.image.load("LES SPRITES/png/LeNinja/NinjaG/Run__009.png")]

# Il faut l'anime(Des etoiles deriÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨re):
bg = pygame.image.load("LES SPRITES/Background/Arene.png")
#
clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.impulsion = 1  # nombre de sauts disponibles
        self.vit = 5
        self.saute = False
        self.left = False
        self.right = False
        self.Shoot = False
        self.Compteurmarche = 0
        self.Compteursaut = 10
        self.standing = True
        self.CompteurSaute = 0
        self.onarena = False  # Sur l'une des arenes:
        # Sur l'une des arenes specifique:
        self.onpetitarena1 = False
        self.onpetitarena2 = False
        self.onhautearena = False
        self.Vie =0
        self.Compteurgravite = 0

    def draw(self, fenetre):





                #Vie:
        arial24= pygame.font.SysFont("arial",25)
        #Ninja:
        VieN=arial24.render(str(Ninja.Vie)+"%",True,pygame.Color(155,155,155))
        fenetre.blit(VieN,(892,575))
        fenetre.blit(pygame.image.load("LES SPRITES/png/LeNinja/Vie/Vie.png"),(920,500))
        #Robot:
        VieR=arial24.render(str(Robot.Vie)+"%",True,pygame.Color(155,155,155))
        fenetre.blit(VieR,(100,575))
        fenetre.blit(pygame.image.load("LES SPRITES/png/LeRobot/Vie/Vie.png"),(0,500))
        #Robot:







        #Animation Robot:
        if Robot.Compteurmarche + 1 >= 24:
            Robot.Compteurmarche = 0



        if not (Robot.standing):
            if Robot.left:
                fenetre.blit(animG[Robot.Compteurmarche // 3], (Robot.x, Robot.y))
                Robot.Compteurmarche += 1

            elif Robot.right:
                fenetre.blit(animD[Robot.Compteurmarche // 3], (Robot.x, Robot.y))
                Robot.Compteurmarche += 1


        else:
            if Robot.right:
                fenetre.blit(animD[0], (Robot.x, Robot.y))


            else:
                fenetre.blit(animG[0], (Robot.x, Robot.y))










        #Animation Ninja:
        if Ninja.Compteurmarche + 1 >= 27:
            Ninja.Compteurmarche = 0

        if not (Ninja.standing):
            if Ninja.left:
                fenetre.blit(animGa[Ninja.Compteurmarche // 3], (Ninja.x, Ninja.y))
                Ninja.Compteurmarche += 1
            elif Ninja.right:
                fenetre.blit(animDr[Ninja.Compteurmarche // 3], (Ninja.x, Ninja.y))
                Ninja.Compteurmarche += 1

        else:
            if Ninja.right:
                fenetre.blit(animDr[0], (Ninja.x, Ninja.y))

            else:

                fenetre.blit(animGa[0], (Ninja.x, Ninja.y))



class projectile(object):
    def __init__(self, x, y, volume, color, facing):
        self.x = x
        self.y = y
        self.volume = volume
        self.color = color
        self.facing = facing
        self.vit = 20 * facing

    def draw(self, fenetre):
        if facing ==1:
            fenetre.blit(Feu[0], (self.x , self.y))
        else:
            fenetre.blit(Feu[1], (self.x , self.y))



def redrawGameWindow():
    fenetre.blit(bg, (0, 0))
    Robot.draw(fenetre)

    for bullet in bullets:
        bullet.draw(fenetre)
    pygame.display.update()


# Personnages
Ninja = Player(600, 300, 64, 64,)

Robot = Player(200, 300, 64, 64,)


# mainloop


run = True
bullets = []
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 1er Personnage:
    for bullet in bullets:
        if 1000 > bullet.x and bullet.x > 0:
            bullet.x += bullet.vit
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        Shoot = True

        if Robot.left:
            facing = -1
        else:
            facing = 1
        if 1 > len(bullets):
            bullets.append(projectile(round(Robot.x + Robot.width // 2),
                                      round(Robot.y + Robot.height // 2), 6, (255, 255, 255), facing))

    if keys[pygame.K_LEFT] and Robot.x > 0:
        Robot.x -= Robot.vit
        Robot.left = True
        Robot.right = False
        Robot.standing = False

    elif keys[pygame.K_RIGHT] and Robot.x < 1000 - Robot.width:
        Robot.x += Robot.vit
        Robot.right = True
        Robot.left = False
        Robot.standing = False

    else:
        Robot.standing = True
        Robot.walkCount = 0

    if not (Robot.saute):
        if keys[pygame.K_UP]:
            Robot.saute = True
            Robot.right = False
            Robot.left = False
            Robot.Compteurmarche = 0

    else:
        if Robot.impulsion == 1:
            if Robot.Compteursaut > 0:
                Robot.y -= (Robot.Compteursaut ** 1.9) * 0.5 + 10
                Robot.Compteursaut -= 1
            else:
                Robot.impulsion -= 1

        else:
            Robot.saute = False
            Robot.Compteursaut = 10

    # Gravite:
    if run:
        if  15> Robot.Compteurgravite:
            Robot.y +=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1



    # Grande arene:
    if 150 < Robot.x < 800 and 315 <= Robot.y <= 325:        #IL FAUT OPTI
        Robot.impulsion = 1
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1


    # Petite arene1:
    if 195 < Robot.x < 390 and 200 <= Robot.y <= 210:
        Robot.impulsion = 1
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1

    # Petit arene2:
    if 540 < Robot.x < 730 and 200 <= Robot.y <= 210:
        Robot.impulsion = 1
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1
    # Haute arene:
    if 370 < Robot.x < 560 and 75 <= Robot.y <= 85:
        Robot.impulsion = 1
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1

    # saut:
    if Robot.onarena:
        Robot.impulsion = 1

    # Respawn:
    if 664 <= Robot.y:
        Robot.x = 200
        Robot.y = 300

    # 2eme personnage:


    if keys[pygame.K_a] and Ninja.x > 0:
        Ninja.x -= Ninja.vit + 2
        Ninja.left = True
        Ninja.right = False
        Ninja.standing= False

    elif keys[pygame.K_d] and Ninja.x < 1000 - Ninja.width:
        Ninja.x += Ninja.vit + 2
        Ninja.right = True
        Ninja.left = False
        Ninja.standing = False

    else:
        Ninja.standing = True
        Ninja.walkCount = 0

    if not (Ninja.saute):
        if keys[pygame.K_w]:
            Ninja.saute = True
            Ninja.right = False
            Ninja.left = False
            Ninja.Compteurmarche = 0

    else:
        if Ninja.impulsion >-1:
            if Ninja.Compteursaut > 0:
                Ninja.y -= (Ninja.Compteursaut ** 1.9) * 0.5 + 10          #CHANTIER
                Ninja.Compteursaut -= 1
            else:
                Ninja.impulsion -= 1


        else:

            Ninja.saute = False
            Ninja.Compteursaut = 10
    # Gravite:
    if run:


        Ninja.y += 10

    # Grande arene:
    if 150 < Ninja.x < 800 and 315 <= Ninja.y <= 325:
        Ninja.impulsion = 2
        Ninja.y -= 10

    # Petite arene1:
    if 195 < Ninja.x < 390 and 200 <= Ninja.y <= 210:
        Ninja.impulsion = 2
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1

    # Petit arene2:
    if 540 < Ninja.x < 730 and 200 <= Ninja.y <= 210:
        Ninja.impulsion = 2
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1
    # Haute arene:
    if 370 < Ninja.x < 560 and 75 <= Ninja.y <= 85:
        Ninja.impulsion = 2
        if  15> Robot.Compteurgravite:
            Robot.y -=(Robot.Compteurgravite)*4
            Robot.Compteurgravite+=1

    # saut:
    if Ninja.onarena:
        Ninja.impulsion = 2
    # Respawn:
    if 664 <= Ninja.y:
        Ninja.x = 600
        Ninja.y = 300

    redrawGameWindow()

pygame.quit()