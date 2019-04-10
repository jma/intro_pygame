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
NOIR = (0, 0, 0)

rectangle = pygame.Rect(200, 300, 90, 10)

ROUGE = (255, 100, 100)
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

    # dessine le rectangle
    pygame.draw.rect(fenetre, ROUGE, rectangle)
    
    
    # mets a jour l'image
    pygame.display.flip()
