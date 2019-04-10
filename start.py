import pygame, sys, time, random
from pygame.locals import *

# initialisation
pygame.init()

# taille de la fenetre
HAUTEUR = 1000
LARGEUR = 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), 0)

# titre de la fenetre
pygame.display.set_caption('Les delicieuses cerises')

# couleurs (rouge, vert, bleu), max 255
NOIR = (000, 000, 000)

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

    # mets a jour l'image
    pygame.display.flip()
