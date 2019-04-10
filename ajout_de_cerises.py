import pygame, sys, time, random
from pygame.locals import *

# initialisation
pygame.init()

# taille de la fenetre
HAUTEUR = 600
LARGEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), 0)

def position_aleatoire():
    return pygame.Rect(random.randint(0, LARGEUR - 10), random.randint(0, HAUTEUR - 10), 20, 20)

# titre de la fenetre
pygame.display.set_caption('Le jeux de Romane')

# couleurs (rouge, vert, bleu), max 255
NOIR = (0, 0, 0)

# parametre de l'ajout des cerises
nombre_de_cerise_au_debut = 20
compteur = 0
vitesse_ajout_des_cerises = 40

# cerise
cerise = pygame.image.load('cherry.png')

# x position aleatoire
cerises_positions = []
for n in range(nombre_de_cerise_au_debut):
    cerises_positions.append(position_aleatoire())

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

    # nouvelles cerises
    compteur += 1
    if compteur == vitesse_ajout_des_cerises:
        # remise a zero du compteur
        compteur = 0
        # ajout d'une cerise
        cerises_positions.append(position_aleatoire())

    # ajouter les cerise dans la fenetre
    for position in cerises_positions:
        fenetre.blit(cerise, position)

    # mets a jour l'image
    pygame.display.flip()
