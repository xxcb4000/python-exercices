

import pygame
pygame.init()

#gestion de la fenêtre (objet)
class fenetre:
    def __init__(self, hauteur, largeur, couleur_de_fond, fps, pas):
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur_de_fond = couleur_de_fond
        self.fps = fps
        self.horloge = pygame.time.Clock()
        self.pas = pas
    
    def tick(self):
        self.horloge.tick(self.fps)

ma_fenetre_de_jeu = fenetre(600,600,(255,255,255), 10, 5)
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))

#gestion d'un anneau (objet)
class unAnneauDuSerpent:
    def __init__ (self, rayon = 5, couleur = (0,255,0)):
        self.rayon = rayon
        self.couleur = couleur

class serpent:
    def __init__(self, taille = 1, direction = 'droite', position_x = ma_fenetre_de_jeu.largeur/2, position_y = ma_fenetre_de_jeu.hauteur/2):
        self.position_x = position_x
        self.position_y = position_y
        self.taille = taille
        self.direction = direction
        self.anneau = unAnneauDuSerpent()
        #self.liste_anneaux = []

    
    def deplacer(self):
        if self.direction == 'haut':
            if self.position_y > 0 :
                self.position_y -= ma_fenetre_de_jeu.pas
            else:
                self.position_y = ma_fenetre_de_jeu.hauteur

        elif self.direction == "bas":
            if self.position_y < ma_fenetre_de_jeu.hauteur:
                self.position_y += ma_fenetre_de_jeu.pas
            else:
                self.position_y = 0

        elif self.direction == "droite":
            if self.position_x < ma_fenetre_de_jeu.largeur:
                self.position_x += ma_fenetre_de_jeu.pas
            else:
                self.position_x = 0

        elif self.direction == "gauche":
            if self.position_x > 0:
                self.position_x -= ma_fenetre_de_jeu.pas
            else:
                self.position_x = ma_fenetre_de_jeu.largeur

    # def grandir(self):
    #     self.taille += 1
    #     self.liste_anneaux.append(self.taille)
        
    def afficher(self):
        #for anneau in self.liste_anneaux:
        pygame.draw.circle(screen, self.anneau.couleur, (self.position_x, self.position_y), self.anneau.rayon)


mon_serpent = serpent()



running = True
#boucle principale du jeu
while running:
    #gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # elif event.type == DEPLACEMENT_SERPENT:
        #     ma_tete_de_serpent.se_deplacer_vers_la_droite()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and mon_serpent.direction != 'bas':
                mon_serpent.direction = 'haut'
            elif event.key == pygame.K_DOWN and mon_serpent.direction != 'haut':
                mon_serpent.direction = 'bas'
            elif event.key == pygame.K_LEFT and mon_serpent.direction != 'droite':
                mon_serpent.direction = 'gauche'
            elif event.key == pygame.K_RIGHT and mon_serpent.direction != 'gauche':
                mon_serpent.direction = 'droite'
    
    screen.fill(ma_fenetre_de_jeu.couleur_de_fond)
    mon_serpent.deplacer()
    mon_serpent.afficher()
    pygame.display.flip()
    ma_fenetre_de_jeu.tick()


pygame.quit()