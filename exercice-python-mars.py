##################################################
## Fonction pour calucler la fréquence des mots ##
##################################################
# from IBM lab

# chaine_a_analyser = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
# Everywhere that Mary went The lamb was sure to go"

# def frequence_mots(chaine):
# '''
# cette fonction analyse le nombre d'occurence de chaque mot dans une string
# '''
#     mots = chaine.lower().replace(',',' ').replace('.',' ').split()
#     frequences = {}
#     for mot in set(mots):
#         frequences[mot] = mots.count(mot)
#     return print(frequences)

# frequence_mots(chaine_a_analyser)



####################
## Calcul du PGCD ##
####################

# # a = int(input("Choisissez les multiples à afficher : "))

# # for i in range(0, 100):
# #     if (i % a) == 0:
# #         print(i)

# # a = int(input("Table de multiplication de : "))
# # b = int(input("Jusque au nombre : "))

# # # print(b//a)

# # for i in range(0, b, a):
# #     print(i)

##############################
## Calcul de Pi Monte-Carlo ##
##############################
#######monte-carlo
# import random
# points_dans_cercle = 0
# nbre_iteration = 10000000

# for i in range(0,nbre_iteration):
#     a = random.random()
#     b = random.random()
#     if (a*a + b*b) <=1:
#         points_dans_cercle = points_dans_cercle + 1

# print(points_dans_cercle)
# pi = points_dans_cercle / nbre_iteration * 4
# print(pi)



###############################
## Des tests de mot de passe ##
###############################

# a = True

# while a :
#     mot_de_passe = input("Veuillez introduire votre mot de passe : ")
#     if len(mot_de_passe) < 15:
#         print("Le mot de passe doit contenir au moins 15 caractères")
#     else:
#         confirmation_mdp = input("Veuillez confirmer votre mot de passe : ")
#         if mot_de_passe != confirmation_mdp:
#             print("Les mots de passe ne correspondent pas")
#         else:
#             print("Votre mot de passe a bien été enregistré")
#             a = False


# a = True
# i = 0
# while  a:
#     entree_utilisateur = input("Veuillez entrer votre mot de passe : ")
#     if entree_utilisateur != mot_de_passe:
#         print("Mot de passe incorrect")
#         i = i + 1
#         if i == 1:
#             print("Deuxième tentative")
#         elif i == 2:
#             print("Troisième et dernière tentative")
#         elif i == 3:
#             print("Mot de passe incorrect 3 fois, veuillez réessayer plus tard")
#             a = False

#     else:
#         print("Mot de passe correct")
#         print("Bienvenue")
#         a = False


# Evaluer des sports achievements

# sport_achievement ={"Serena Williams":23, "Lionel Messi":7, "Michael Phelps":23, "Usain Blot":8, "Roger Federer":20, "Cristiano Ronaldo":5}
# a = input("Nous allons vérifier si un sportif a plus de 10 achievements. Quel sportif voulez-vous vérifier ?")
# if a in sport_achievement.keys() and  sport_achievement[a]>=10:
#     print(f"Oui ! {a} a plus de 10 achievements.")
# elif a in sport_achievement.keys():
#     print(f"Non, {a} est dans la liste mais en-dessous des 10 achievements.")
# else: 
#     b = input(f"{a} n'est pas dans la liste, voulez-vous l'ajouter ?")

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "violet"]
# for color in (colors):
#     print(color)


# fruits = ["apple", "banana", "orange"]
# for index, fruit in fruits:
#     print(f"At position {index}, I found a {fruit}")





# def greet(name):
#     return "Hello, " + name

# print(greet("Vincent"))
# global_variable = "I'm global"
# def example_function():
#     local_variable = "I'm local"
#     print(global_variable)  # Accessing global variable
#     print(local_variable)   # Accessing local variable


# example_function()
# example_function()

# def greet(name):
#     return "Hello, " + name
# for _ in range(3):
#     print(greet("Alice"))

# 

