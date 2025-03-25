

import pygame
pygame.init()

#gestion de la fenêtre (objet)
class Fenetre:
    def __init__(self, hauteur, largeur, couleur_de_fond, horloge, pas):
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur_de_fond = couleur_de_fond
        self.horloge = horloge
        self.pas = pas

ma_fenetre_de_jeu = Fenetre(600,600,(255,255,255), 60, 8)
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))

#gestion d'un anneau (objet)
class unAnneauDuSerpent:
    def __init__ (self, position_x = ma_fenetre_de_jeu.largeur/2, position_y = ma_fenetre_de_jeu.hauteur/2, taille = 8, couleur = (0,255,0)):
        self.position_x = position_x
        self.position_y = position_y
        self.taille = taille
        self.couleur = couleur

    def se_deplacer_vers_la_gauche(self):
        self.position_x -= ma_fenetre_de_jeu.pas
    def se_deplacer_vers_la_droite(self):
        self.position_x += ma_fenetre_de_jeu.pas
    def se_deplacer_vers_le_haut(self):
        self.position_y -= ma_fenetre_de_jeu.pas
    def se_deplacer_vers_le_bas(self):
        self.position_y += ma_fenetre_de_jeu.pas
    def afficher(self):
        pygame.draw.circle(screen, self.couleur, (self.position_x,self.position_y), self.taille)

ma_tete_de_serpent = unAnneauDuSerpent()
DEPLACEMENT_SERPENT = pygame.USEREVENT + 1

#gestion du jeu
class jeu:
    def __init__(self, running, direction, vitesse):
        self.running = True
        self.direction = 'Droite'
        self.vitesse = 200
        pygame.time.set_timer(DEPLACEMENT_SERPENT, self.vitesse)

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == DEPLACEMENT_SERPENT:
                ma_tete_de_serpent.se_deplacer_vers_la_droite()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ma_tete_de_serpent.se_deplacer_vers_le_haut()
                elif event.key == pygame.K_DOWN:
                    ma_tete_de_serpent.se_deplacer_vers_le_bas()
                elif event.key == pygame.K_LEFT:
                    ma_tete_de_serpent.se_deplacer_vers_la_gauche()
                elif event.key == pygame.K_RIGHT:
                    ma_tete_de_serpent.se_deplacer_vers_la_droite()

    def afficher(self):
        screen.fill((255,255,255))
        ma_tete_de_serpent.afficher()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

mon_jeu = jeu(True, 'Droite', 200)



#boucle principale du jeu
while mon_jeu.running:
    #gestion des événements
    mon_jeu.gestion_evenements()


    #affichage à l'écran
    mon_jeu.afficher()


pygame.quit()