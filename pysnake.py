

import pygame
pygame.init()

class Fenetre:
    def __init__(self, hauteur, largeur, couleur_de_fond):
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur_de_fond = couleur_de_fond

ma_fenetre_de_jeu = Fenetre(600,600,(255,255,255))
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))

class unAnneauDuSerpent:
    def __init__ (self, position_x = ma_fenetre_de_jeu.largeur/2, position_y = ma_fenetre_de_jeu.hauteur/2, taille = 9, couleur = (0,255,0)):
        self.position_x = position_x
        self.position_y = position_y
        self.taille = taille
        self.couleur = couleur
    
    def se_deplacer_vers_la_gauche(self):
        self.position_x -= 1
    def se_deplacer_vers_la_droite(self):
        self.position_x += 1
    def se_deplacer_vers_le_haut(self):
        self.position_y += 1
    def se_deplacer_vers_le_bas(self):
        self.position_y -= 1

    


ma_tete_de_serpent = unAnneauDuSerpent()



#boucle principale du jeu
running = True
while running:
    #gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ma_tete_de_serpent.se_deplacer_vers_le_haut()
    elif keys[pygame.K_DOWN]:
        ma_tete_de_serpent.se_deplacer_vers_le_bas()
    elif keys[pygame.K_LEFT]:
        ma_tete_de_serpent.se_deplacer_vers_la_gauche()
    elif keys[pygame.K_RIGHT]:
        ma_tete_de_serpent.se_deplacer_vers_la_droite()
    
    #mise à jour


    #dessin à l'écran
    screen.fill((255,255,255))
    pygame.draw.circle(screen, ma_tete_de_serpent.couleur, (ma_tete_de_serpent.position_x,ma_tete_de_serpent.position_y), ma_tete_de_serpent.taille)
    pygame.display.flip()

pygame.quit()