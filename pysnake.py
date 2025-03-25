

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

ma_fenetre_de_jeu = fenetre(600,600,(255,255,255), 10, 10)
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))

#gestion d'un anneau (objet)
class unAnneauDuSerpent:
    def __init__ (self, rayon = 5, couleur = (0,255,0), position_x = 300, position_y = 300, direction = 'droite', taille = 1):
        self.position_x = position_x
        self.position_y = position_y
        self.rayon = rayon
        self.couleur = couleur
        self.direction = direction
        self.taille = taille
        self.former_position_x = []
        self.former_position_y = []

    def creer(self):
        self.former_position_x.append(self.position_x)
        self.former_position_y.append(self.position_y)
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

    def dessiner(self):            
        pygame.draw.circle(screen, self.couleur, (self.position_x, self.position_y), self.rayon)

    def grandir(self):
        for i in range(0, self.taille):
            pygame.draw.circle(screen, self.couleur, (self.former_position_x[i], self.former_position_y[i]), self.rayon)
        
        self.taille += 1  
    
        
running = True
nouvel_anneau = unAnneauDuSerpent()
#boucle principale du jeu
while running:
    #gestion des événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and nouvel_anneau.direction != 'bas':
                nouvel_anneau.direction = 'haut'
            elif event.key == pygame.K_DOWN and nouvel_anneau.direction != 'haut':
                nouvel_anneau.direction = 'bas'
            elif event.key == pygame.K_LEFT and nouvel_anneau.direction != 'droite':
                nouvel_anneau.direction = 'gauche'
            elif event.key == pygame.K_RIGHT and nouvel_anneau.direction != 'gauche':
                nouvel_anneau.direction = 'droite'
            elif event.key == pygame.K_SPACE:
                nouvel_anneau.grandir()
    
    screen.fill(ma_fenetre_de_jeu.couleur_de_fond)
    nouvel_anneau.creer()
    nouvel_anneau.dessiner()
    nouvel_anneau.grandir()

    pygame.display.flip()
    ma_fenetre_de_jeu.tick()


pygame.quit()