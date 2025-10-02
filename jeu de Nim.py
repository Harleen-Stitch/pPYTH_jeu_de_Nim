liste = [1, 2, 3]
allumettes = 0

def initialisation(allumettes):
    print('Règle du jeu : Enlevez 1, 2 ou 3 allumettes par tour. Celui qui enlève la dernière allumette à gagner !')
    allumettes = int(input("Saisissez un nombre impair d'allumettes entre 5 et 99 : "))
    while allumettes % 2 == 0:
        print("Ce n'est pas impair.")
        allumettes = int(input("Saisissez un nombre impair d'allumettes : "))
    while allumettes < 5 or allumettes > 99:
        print("Ce n'est pas compris entre 5 et 99")
        allumettes = int(input("Saisissez un nombre impair d'allumettes entre 5 et 99 : "))
        print(f'Le plateau comporte {allumettes} allumettes.')
    return allumettes
    
def joueur1():
    joueur1 = int(input("Voulez-vous commencer (1) ou que l'ordinateur commence (2)?"))
    while joueur1 <1 or joueur1 >2:
        print("Impossible.")
        joueur1 = int(input("Tapez 1 ou 2 ? "))
    if joueur1 == 1:
        print("C'est à vous de commencer")
    else:
        print("A l'ordinateur de commencer.")
    return joueur1


def afficher_plateau(allumettes):
    print(f'Il reste {allumettes} allumettes.')
    print(allumettes * "|")

#jusque là, c'est ok

def tour(joueur1, allumettes):
    while allumettes > 1:
        if joueur1 == 1 :
            allumettes = tour_joueur(allumettes)
            joueur1 = 2
            afficher_plateau(allumettes) #coté joueur validé
        else:
            allumettes = tour_ordi(allumettes)
            joueur1 = 1
            afficher_plateau(allumettes)
    if allumettes == 1 or allumettes == 0:
        if joueur1==1:
            print("Vous avez perdu...")
        else:
            print("Vous avez gagné !")



def tour_joueur(allumettes):
    print("A vous de jouer !")
    a = int(input("Combien prenez-vous d'allumettes? " ))
    while a not in liste:
        print("Impossible.")
        a = int(input("Combien prenez-vous d'allumettes? 1, 2 ou 3 : " ))       
    allumettes = allumettes - a
    print(allumettes) #jusqu'ici, c'est ok
    return allumettes


def tour_ordi(allumettes):
    print("Au tour de l'ordinateur.")
    # temp = str(allumettes)
    liste = list(str(allumettes))
    liste.append(0)
    add = int(liste[0]) + int(liste[1])
    while add > 3:
        a = int(add /3)
        add = a
    print(f"L'ordinateur joue {add} allumettes")
    allumettes -= add
    return allumettes


allumettes = initialisation(allumettes)
afficher_plateau(allumettes) #jusque là, c'est ok
joueur1 = joueur1()
tour(joueur1, allumettes) #j'arrive à avoir d puis e selon qui joue OU e
print("Fin du jeu")
      
