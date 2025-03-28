

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
        if abs(prochaine_position[0] - ma_pomme.position_x) <5 and  abs(prochaine_position[1] - ma_pomme.position_y) <5:
            mon_serpent.grandir()
            ma_pomme.couleur = (255,255,255)
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
    def __init__(self, position_x = -10, position_y= -10, rayon = 5, couleur =(255,0,0), duree = 5):
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

class ui:
    def __init__(self, largeur, hauteur, position_x, position_y, actif, texte, couleur_boite, couleur_texte, actions):
        self.largeur = largeur
        self.hauteur = hauteur
        self.position_x = position_x
        self.position_y = position_y
        self.actif = actif
        self.texte = texte
        self.couleur_boite = couleur_boite
        self.couleur_texte = couleur_texte
        self.actions = actions
    
    def creer(self):
        le_rect = pygame.draw.rect(screen, self.couleur_boite, (ma_fenetre_de_jeu.largeur/2 - self.largeur/2,  self.position_y, self.largeur, self.hauteur),0,10)
        le_rect
        if self.texte:
            font = pygame.font.SysFont(None, 40)
            texte_in = font.render(self.texte, True, self.couleur_texte)  
            screen.blit(texte_in, ((ma_fenetre_de_jeu.largeur/2 - texte_in.get_width()/2), self.position_y + self.hauteur/2 - texte_in.get_height()/2 +3)) 
        if le_rect.collidepoint(pygame.mouse.get_pos()) and self.actif:
            self.couleur_boite = (81, 127, 12)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    global running
                    global menu
                    running = True
                    menu = False

        elif self.actif:
            self.couleur_boite = (81, 100, 12)

        #if le_rect.collidepoint(pygame.mouse.get_pos()
        #if self.actif:



#initialisation du jeu
mon_serpent = serpent()
ma_pomme = pomme()
ma_boite_globale = ui(300,300, 0, 100, False, '' , (55, 76, 22), (255,255,255), False)
ma_boite_commencer = ui(250,50, 0, ma_boite_globale.position_y+20, True, 'Commencer' , (81, 127, 12), (255,255,255), False)
ma_boite_meilleurs_scores = ui(250,50, 0, ma_boite_commencer.position_y +70, True, 'Meilleurs scores', (81, 127, 12),(255,255,255), False)
ma_boite_auto_pilote = ui(250,50, 0, ma_boite_meilleurs_scores.position_y +70, True, 'Auto-pilote', (81, 127, 12),(255,255,255), False)
ma_boite_quitter = ui(250,50, 0, ma_boite_auto_pilote.position_y +70, True, 'Quitter', (81, 127, 12),(255,255,255), False)
# ma_boite_commencer = 
# ma_boite_meilleurs_scores =
# ma_boite_quitter = 
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

        ma_boite_globale.creer()
        ma_boite_commencer.creer()
        ma_boite_meilleurs_scores.creer()
        ma_boite_auto_pilote.creer()
        ma_boite_quitter.creer()
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
        ma_pomme.ajouter()
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