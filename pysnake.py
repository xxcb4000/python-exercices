

#code_source_snake_pythonique = """

import pygame
from random import randrange
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


#boucle du menu
ma_fenetre_de_jeu = fenetre(600,600,(255,255,255), 15, 10)
screen = pygame.display.set_mode((ma_fenetre_de_jeu.largeur,ma_fenetre_de_jeu.hauteur))


#ma classe serpent
class serpent:
    def __init__(self, rayon = 5, couleur = (20,148,20), taille= 4, direction = 'droite', index = 0):
        self.rayon = rayon
        self.couleur = couleur
        self.taille = taille
        self.direction = direction
        self.positions = [(270,300),(280,300),(290,300),(300,300)]
        self.index = index
    
    def avancer(self):
        prochaine_position = self.calcul_nouvelles_coordonnées(self.positions[self.index-1][0], self.positions[self.index-1][1], self.direction)
        if abs(prochaine_position[0] - mes_pommes.position_x) <5 and  abs(prochaine_position[1] - mes_pommes.position_y) <5:
            mon_serpent.grandir()
            mes_pommes.couleur = (255,255,255)
        elif prochaine_position in self.positions:
            global pause
            pause = True
        self.positions[self.index] = self.calcul_nouvelles_coordonnées(self.positions[self.index-1][0], self.positions[self.index-1][1], self.direction)
        self.index = (self.index + 1) % self.taille

    def calcul_nouvelles_coordonnées(self, position_x, position_y, direction):
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

    def dessiner(self):
        for i in range(0, self.taille):
            pygame.draw.circle(screen, self.couleur, (self.positions[i][0], self.positions[i][1]), self.rayon)

    def grandir(self):
        self.positions.append(self.positions[self.index-1])
        self.taille += 1


class pomme:
    def __init__(self, position_x = -10, position_y= -10, rayon = 8, couleur =(255,0,0), duree = 5):
        self.position_x = position_x
        self.position_y = position_y
        self.rayon = rayon
        self.couleur = couleur
        self.duree = duree
        self.apparition = 0

    def ajouter(self):
        maintenant = pygame.time.get_ticks()
        if maintenant - self.apparition > self.duree*1000:
            self.couleur = (255,0,0)
            self.position_x = randrange(ma_fenetre_de_jeu.pas, ma_fenetre_de_jeu.largeur-ma_fenetre_de_jeu.pas, ma_fenetre_de_jeu.pas)
            self.position_y = randrange(ma_fenetre_de_jeu.pas, ma_fenetre_de_jeu.hauteur-ma_fenetre_de_jeu.pas, ma_fenetre_de_jeu.pas)
            self.apparition = pygame.time.get_ticks()
        pygame.draw.circle(screen, self.couleur, (self.position_x, self.position_y), self.rayon)


#initialisation du jeu
mon_serpent = serpent()
mes_pommes = pomme()
global pause
global running
global menu
running = True
pause = False
menu = True

#boucle principale du jeu
while running:


    while menu:
        screen.fill(ma_fenetre_de_jeu.couleur_de_fond)
        pygame.draw.rect(screen, (56, 111, 72), (ma_fenetre_de_jeu.largeur/2 - 400/2, ma_fenetre_de_jeu.hauteur/2 - 300/2, 400, 300))
        font = pygame.font.SysFont(None, 20)
        texte = font.render("Appuyez sur ""Espace"" pour commencer", True, (255, 255, 255))  
        screen.blit(texte, (150, 250)) 
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    menu = False
                    running = True
                    pause = False

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
                menu = True
    


    
    #gestion du serpent
    if not pause:
        screen.fill(ma_fenetre_de_jeu.couleur_de_fond)
        mes_pommes.ajouter()
        mon_serpent.avancer()
        mon_serpent.dessiner()
        #affichage
        pygame.display.flip()
        #horloge
        ma_fenetre_de_jeu.tick()
    



pygame.quit() #"""


# sauvegarde = 'sauvegarde_snake_pythonique.txt'
# with open(sauvegarde, 'w') as sauvegarde:
#     sauvegarde.write(code_source_snake_pythonique)