

#code_source_snake_pythonique = """

import pygame
pygame.init()

#ma classe fenêtre
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

#mon objet fenêtre
ma_fenetre_de_jeu = fenetre(600,600,(255,255,255), 25, 10)
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))

#ma fonction pour calculer les coordonnées du nouvel anneau du serpent à afficher
def calcul_nouvelles_coordonnées(position_x, position_y, direction):
        if direction == 'haut':
            if position_y > 0 :
                position_y -= ma_fenetre_de_jeu.pas
            else:
                position_y = ma_fenetre_de_jeu.hauteur

        elif direction == "bas":
            if position_y < ma_fenetre_de_jeu.hauteur:
                position_y += ma_fenetre_de_jeu.pas
            else:
                position_y = 0

        elif direction == "droite":
            if position_x < ma_fenetre_de_jeu.largeur:
                position_x += ma_fenetre_de_jeu.pas
            else:
                position_x = 0

        elif direction == "gauche":
            if position_x > 0:
                position_x -= ma_fenetre_de_jeu.pas
            else:
                position_x = ma_fenetre_de_jeu.largeur
        return(position_x, position_y)

#ma classe serpent
class serpent:
    def __init__(self, rayon = 5, couleur = (0,255,0), taille= 4, direction = 'droite', position_init = (300,300), index = 0):
        self.rayon = rayon
        self.couleur = couleur
        self.taille = taille
        self.direction = direction
        self.positions = [(270,300),(280,300),(290,300),(300,300)]
        self.index = index
    
    def avancer(self):
        self.positions[self.index] = calcul_nouvelles_coordonnées(self.positions[self.index-1][0], self.positions[self.index-1][1], self.direction)
        self.index = (self.index + 1) % self.taille

    def dessiner(self):
        for i in range(0, self.taille):
            pygame.draw.circle(screen, self.couleur, (self.positions[i][0], self.positions[i][1]), self.rayon)

    def grandir(self):
        self.positions.append(self.positions[self.index])
        self.taille += 1

#mon objet serpent
mon_serpent = serpent()

running = True

#boucle principale du jeu
while running:

    #gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #gestion des touches
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and mon_serpent.direction != 'bas':
                mon_serpent.direction = 'haut'
            elif event.key == pygame.K_DOWN and mon_serpent.direction != 'haut':
                mon_serpent.direction = 'bas'
            elif event.key == pygame.K_LEFT and mon_serpent.direction != 'droite':
                mon_serpent.direction = 'gauche'
            elif event.key == pygame.K_RIGHT and mon_serpent.direction != 'gauche':
                mon_serpent.direction = 'droite'
            elif event.key == pygame.K_SPACE:
                mon_serpent.grandir()
    
    #fond blanc
    screen.fill(ma_fenetre_de_jeu.couleur_de_fond)
    
    #gestion du serpent

    mon_serpent.avancer()
    mon_serpent.dessiner()
    #mon_serpent.grandir()

    #affichage
    pygame.display.flip()

    #horloge
    ma_fenetre_de_jeu.tick()

pygame.quit() #"""


# sauvegarde = 'sauvegarde_snake_pythonique.txt'
# with open(sauvegarde, 'w') as sauvegarde:
#     sauvegarde.write(code_source_snake_pythonique)