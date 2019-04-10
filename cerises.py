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
NOIR = (150, 255, 100)

# cerise
cerise = pygame.image.load('cherry.png')


# 20 position aleatoire
cerises_positions = []
for n in range(30):
    position = pygame.Rect(random.randint(0, LARGEUR - 20), random.randint(0, HAUTEUR - 20), 20, 20)
    cerises_positions.append(position)

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

    # ajouter les cerise un peu partout
    for position in cerises_positions:
        fenetre.blit(cerise, position)

    # mets a jour l'image
    pygame.display.flip()
