import pygame, sys, time, random
from pygame.locals import *

# initialisation
pygame.init()

# taille de la fenetre
HAUTEUR = 600
LARGEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), 0)

# titre de la fenetre
pygame.display.set_caption('Le jeux de Romane')

# couleurs (rouge, vert, bleu), max 255
NOIR = (50, 255, 150)

# cerise
cerise = pygame.image.load('burger.png')

# position au centre
#cerise_position = pygame.Rect(LARGEUR/2 - 10, HAUTEUR/2 - 10, 20, 20)

# position aleatoire
cerise_position = pygame.Rect(random.randint(0, LARGEUR - 20), random.randint(0, HAUTEUR - 20), 40, 40)

while True:

    # capturer les evenements clavier et souris
    for event in pygame.event.get():

        # pour quitter l'application
        # boutton fenetre
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # touche "q"
        if event.type == KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()


    # couleur de fond de la fenetre
    fenetre.fill(NOIR)

    # ajouter une cerise a une position
    fenetre.blit(cerise, cerise_position)

    # mets a jour l'image
    pygame.display.flip()
