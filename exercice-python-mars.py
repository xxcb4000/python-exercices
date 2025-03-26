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


#test compte string
# def freq(string,passedkey):

#     #step1: A list variable is declared and initialized to an empty list.
#     words = []

#     #step2: Break the string into list of words
#     words = string.split() # or string.lower().split()

#     #step3: Declare a dictionary
#     Dict = {}

#     #step4: Use for loop to iterate words and values to the dictionary
#     for key in words:
#         if(key == passedkey):
#             Dict[key] = words.count(key)   
#     #step5: Print the dictionary
#     print("Total Count:",Dict)

#step6: Call function and pass string in it
# freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
# Everywhere that Mary went The lamb was sure to go","little")


#print(len('example'))

# text = "example"
# length = len(text)  # No AttributeError, correct method usage

# # using Try- except 
# try:
#     # Attempting to divide 10 by 0
#     result = 10 / 0
# except ZeroDivisionError:
#     # Handling the ZeroDivisionError and printing an error message
#     print("Error: Cannot divide by zero")
# # This line will be executed regardless of whether an exception occurred
# print("outside of try and except block")


################################################
## Gestion des erreurs - ex: division et sqrt ##
################################################

# def safe_division():
#         numerator = int(input("Introduisez le numérateur:"))
#         denominator = int(input("Introduisez le dénominateur:"))
#         try:
#             result = numerator/denominator
#         except ZeroDivisionError:
#             print('Erreur : division par 0')
#         except ValueError:
#             print('Vous devez introduire un nombre')
#         else:
#             print("Ca a marché !", result)
#             return result
#         finally:
#             print("Safe_divison a fait le taf !")

# safe_division()

# import math

# def safe_square():
#             a = float(input('Entrez un nombre : '))
#     try :
#         result = math.sqrt(a)
#     except ValueError :
#         print("Tu as entré un ", type(a))
#     except :
#         print("Y a quelque chose qui ne va pas mother fucker")
#     else :
#         return result


# safe_square()


###############################################
## Analyse fréquence mots - POO - texte wiki ##
###############################################

# texte_a_analyser = "La périphrase la plus souvent utilisée pour désigner " \
# "la ville de Liège est « Cité Ardente ». Cette appellation vient du titre " \
# "d'un roman chevaleresque écrit par Henry Carton de Wiart édité en 1904. " \
# "Ce roman raconte le sac de la ville de Liège par les troupes de Charles le " \
# "Téméraire en 1468, malgré la résistance liégeoise, aidée par un important contingent, " \
# "les Six cents Franchimontois, venu d'une seigneurie voisine. L'appellation " \
# "de « Cité Ardente[note 2] » n'est pas antérieure à la parution de ce roman[4]. " \
# "Elle a surtout été popularisée par le prince Albert qui, faisant référence au titre " \
# "dudit roman dans son discours inaugural de l'Exposition universelle de Liège de 1905, " \
# "lance vraiment l'expression auprès des journalistes liégeois. Cette expression est " \
# "restée ancrée dans le langage populaire et la littérature[5]. Outre « Cité Ardente », " \
# "Liège est souvent appelée « La Cité des Princes-évêques » en raison de l'ancienne " \
# "principauté épiscopale de Liège et de l'esprit des Liégeois que l'on qualifie d'esprit " \
# "principautaire. Liège est, tout comme Rouen, Caen, Poitiers, Dijon, Montréal, " \
# "Vienne ou Prague, surnommée la Ville aux Cent Clochers en raison du nombre important " \
# "d'édifices religieux : une cathédrale, six collégiales et une cinquantaine d'églises. " \
# "En raison de ses grands liens d'amitié avec la France — les Liégeois s'étant inspiré de " \
# "la Révolution parisienne de 1789 et ayant par la suite été la première ville étrangère " \
# "à recevoir la Légion d'honneur —, elle est parfois appelée « Le Petit Paris » mais aussi " \
# "« La petite France des bords de Meuse » par Jules Michelet, ou encore « Un petit coin de " \
# "France perdu en Belgique » par Alexandre Dumas. Enfin, Liège a été aussi surnommée " \
# "l'« Athènes du Nord » en raison des écoles qui font sa renommée dans toute l'Europe au Moyen Âge."



# class analyseFrequenceMots:
#     def __init__(self, texte):
#         self.listeMots = texte.replace(',', ' ').replace('.', ' ').replace('[', ' ').replace(']', ' ').replace("'",' ').lower().split(' ')
    
#     def frequence_mots(self):
#         frequence_mots = {}
#         for mot in set(self.listeMots):
#             frequence_mots[mot] = self.listeMots.count(mot)
#         return frequence_mots
    
#     def frequence_un_mot(self, mot):
#         frequence_mot = self.listeMots.count(mot)
#         return frequence_mot

# monAnalyseur = analyseFrequenceMots(texte_a_analyser)

# print(monAnalyseur.frequence_mots())
# print(monAnalyseur.frequence_un_mot('liège'))


#################################################################
## Test lecture/écriture fichier - mise à jour fichier membres ##
#################################################################


# my_file = 'my_file.txt'
# with open(my_file, 'w') as file:
#     file.write('Coucou mon nouveau fichier\n Et voici une nouvelle ligne \n Bravo Vincent lol mother fucker')

# with open(my_file, 'r') as file:
#     print(file.read())


## on génère les fichiers de membres

# from random import randint

# fichier_des_membres = 'fichier_des_membres.txt'
# fichier_des_ex_membres = 'fichier_des_ex_membre.txt'

# with open(fichier_des_membres, 'w') as fichier_des_membres:
#     fichier_des_membres.write('Numero_de_membre     date_inscription      en_ordre\n')
#     for i in range(20):
#         numero = str(randint(1,1000))
#         date_annee = str(randint(1990, 2020))
#         date_mois = str(randint(1,12))
#         date_jour = str(randint(1,28))
#         date = date_jour + '-' + date_mois + '-' + date_annee
#         en_ordre = 'oui' if bool(randint(0,1)) else 'non'
#         ligne_traitee = f'{numero:^20}{date:<22}{en_ordre:<10} \n'
#         fichier_des_membres.write(ligne_traitee)

# with open(fichier_des_ex_membres, 'w') as fichier_des_membres:
#     fichier_des_membres.write('Numero_de_membre     date_inscription      en_ordre\n')
#     for i in range(15):
#         numero = str(randint(1,1000))
#         date_annee = str(randint(1990, 2020))
#         date_mois = str(randint(1,12))
#         date_jour = str(randint(1,28))
#         date = date_jour + '-' + date_mois + '-' + date_annee
#         en_ordre = 'non'
#         ligne_traitee = f'{numero:^20}{date:<22}{en_ordre:<10} \n'
#         fichier_des_membres.write(ligne_traitee)

## on les met à jour

# fichier_des_membres = 'fichier_des_membres.txt'
# fichier_des_ex_membres = 'fichier_des_ex_membre.txt'
# fichier_des_membres_maj = 'fichier_des_membres_maj.txt'

# with open(fichier_des_membres, 'r') as fichier_des_membres:
#         liste_vrac_fdm = fichier_des_membres.read().split()
#         liste_tuple_fdm = []
#         liste_tuple_exfdm_from_fdm = []
#         for i in range(0,63, 3):
#             liste_tuple_fdm.append((liste_vrac_fdm[i], liste_vrac_fdm[i+1], liste_vrac_fdm[i+2]))
#         i = 0
#         while i <= (len(liste_tuple_fdm)-1):
#             if liste_tuple_fdm[i][2] == 'non':
#                 liste_tuple_exfdm_from_fdm.append(liste_tuple_fdm[i])
#                 del (liste_tuple_fdm[i])
#                 i -=1 
#             i+=1
  
#         print(liste_tuple_fdm)
#         print(len(liste_tuple_fdm))
#         print(liste_tuple_exfdm_from_fdm)
#         print(len(liste_tuple_exfdm_from_fdm))

# with open(fichier_des_membres_maj, 'w') as fichier_des_membres:
#      for membre in liste_tuple_fdm:
#         fichier_des_membres.write(f'{(membre[0]):^20}{str(membre[1]):<22}{str(membre[2]):<10}\n')

# with open(fichier_des_ex_membres, 'a') as fichier_des_ex_membres:
#      for i in range(0,i):
#         fichier_des_ex_membres.write(f'{(liste_tuple_exfdm_from_fdm[i][0]):^20}{str(liste_tuple_exfdm_from_fdm[i][1]):<22}{str(liste_tuple_exfdm_from_fdm[i][2]):<10}\n')