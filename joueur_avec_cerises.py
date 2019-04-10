import pygame, sys, time, random
from pygame.locals import *

# initialisation
pygame.init()

# taille de la fenetre
HAUTEUR = 400
LARGEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), 0)

def position_aleatoire(taille=20):
    return pygame.Rect(random.randint(0, LARGEUR - (taille/2)), random.randint(0, HAUTEUR - (taille/2)), taille, taille)

# titre de la fenetre
pygame.display.set_caption('Le jeux de Romane')

# couleurs (rouge, vert, bleu), max 255
NOIR = (100, 100, 255)

bruit = pygame.mixer.Sound('son.wav')

perdu = pygame.image.load('game_over.png')
fond = pygame.image.load('fond.png')
fond = pygame.transform.scale(fond, (LARGEUR, HAUTEUR))
# perdu = pygame.transform.scale(perdu, (perdu_image.width, perdu_image.heigh))
perdu_position = perdu.get_rect()
perdu_position.centerx = HAUTEUR/2
perdu_position.centery = LARGEUR/2

FIN_DU_JEU = False

#----------------------------------------------
#------------------ Joueur --------------------
#----------------------------------------------
# joueur
taille_du_joueur = 30
image_joueur = pygame.image.load('beau_gosse.png')
joueur = pygame.transform.scale(image_joueur, (taille_du_joueur, taille_du_joueur))

# position aleatoire
joueur_position = position_aleatoire(taille_du_joueur)

# mouvements
VITESSE_DE_MOUVEMENT = 10
aller_a_droite = False
aller_a_gauche = False
aller_en_haut = False
aller_en_bas = False

#----------------------------------------------
#------------------ Cerises --------------------
#----------------------------------------------
# parametre de l'ajout des cerises
nombre_de_cerise_au_debut = 30
compteur = 0
vitesse_ajout_des_cerises = 100

# cerise
cerise = pygame.image.load('burger.png')

# x position aleatoire
cerises_positions = []
for n in range(nombre_de_cerise_au_debut):
    cerises_positions.append(position_aleatoire())

score = 0
while True:

    pygame.display.set_caption("L'acro aux burgers, Score: %s" % score)
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
##            aller_a_droite = False
##            aller_a_gauche = False
##            aller_en_haut = False
##            aller_en_bas = False

            # les touches de mouvements
            if event.key == K_LEFT:
                aller_a_gauche = True
            if event.key == K_RIGHT:
                aller_a_droite = True
            if event.key == K_UP:
                aller_en_haut = True
            if event.key == K_DOWN:
                aller_en_bas = True
            if event.key == ord('p'):
                aller_a_droite = True
                aller_en_bas = True
    fenetre.blit(fond, (0, 0))        
    # fin du jeu
    if FIN_DU_JEU:
        fenetre.blit(perdu, perdu_position)
        pygame.display.flip()
        continue

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
##    fenetre.fill(NOIR)

    # ajouter le joueur a une position
    fenetre.blit(joueur, joueur_position)

    # nouvelles cerises
    compteur += 1
    if compteur == vitesse_ajout_des_cerises:
        # remise a zero du compteur
        compteur = 0
        # ajout d'une cerise
        cerises_positions.append(position_aleatoire())
        joueur_position.inflate_ip(-4, -4)
        try:
            joueur = pygame.transform.scale(image_joueur, (joueur_position.width, joueur_position.height))
        except ValueError:
            FIN_DU_JEU = True

    # supprime les cerises touchees par le joueur
    for position in cerises_positions:
        if joueur_position.colliderect(position):
            score += 1
            cerises_positions.remove(position)
            bruit.play()
            joueur_position.inflate_ip(4, 4)
            joueur = pygame.transform.scale(image_joueur, (joueur_position.width, joueur_position.height))

    # ajouter les cerise dans la fenetre
    for position in cerises_positions:
        fenetre.blit(cerise, position)

    # mets a jour l'image
    pygame.display.update()
