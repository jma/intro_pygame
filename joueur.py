import pygame, sys, time, random
from pygame.locals import *

# initialisation
pygame.init()

# taille de la fenetre
HAUTEUR = 600
LARGEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), 0)

def position_aleatoire(taille=20):
    return pygame.Rect(random.randint(0, LARGEUR - (taille/2)), random.randint(0, HAUTEUR - (taille/2)), taille, taille)

# titre de la fenetre
pygame.display.set_caption('Le jeux de Romane')

# couleurs (rouge, vert, bleu), max 255
NOIR = (0, 0, 0)

# joueur
taille_du_joueur = 40
joueur = pygame.image.load('beau_gosse.png')
joueur = pygame.transform.scale(joueur, (taille_du_joueur, taille_du_joueur))

# position aleatoire
joueur_position = position_aleatoire(taille_du_joueur)

# mouvements
VITESSE_DE_MOUVEMENT = 1
aller_a_droite = False
aller_a_gauche = False
aller_en_haut = False
aller_en_bas = False

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

            # arreter le mouvement quand on relache la touche
            if event.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN, ord('p')]:
                aller_a_droite = False
                aller_a_gauche = False
                aller_en_haut = False
                aller_en_bas = False

        if event.type == KEYDOWN:

            # arreter les mouvements
            aller_a_droite = False
            aller_a_gauche = False
            aller_en_haut = False
            aller_en_bas = False
            if event.key == ord('p'):
                aller_a_droite = True
                aller_en_bas = True
            # les touches de mouvements
            if event.key == K_LEFT:
                aller_a_gauche = True
            if event.key == K_RIGHT:
                aller_a_droite = True
            if event.key == K_UP:
                aller_en_haut = True
            if event.key == K_DOWN:
                aller_en_bas = True

    # deplacements
    if aller_en_bas:
        joueur_position.bottom += VITESSE_DE_MOUVEMENT
        #joueur_position.bottom = min(joueur_position.bottom, HAUTEUR)
    if aller_en_haut:
        joueur_position.top -= VITESSE_DE_MOUVEMENT
        #joueur_position.top = max(joueur_position.top, 0)
    if aller_a_gauche:
        joueur_position.left -= VITESSE_DE_MOUVEMENT
        #joueur_position.left = max(joueur_position.left, 0)
    if aller_a_droite:
        joueur_position.right += VITESSE_DE_MOUVEMENT
        #joueur_position.right = min(joueur_position.right, LARGEUR)

    # couleur de fond de la fenetre
    fenetre.fill(NOIR)

    # ajouter le joueur a une position
    fenetre.blit(joueur, joueur_position)

    # mets a jour l'image
    pygame.display.flip()
