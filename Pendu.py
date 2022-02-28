import math
import random
import os


liste_mots = ["furet",
    "migale",
    "diphtongue",
    "elegance",    
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

startAgain = True

while startAgain == True :

    motsChoisi = liste_mots[random.randrange(len(liste_mots))]
    nombre_de_chance = len(motsChoisi)
    MotsEnCours = ""

    for u in motsChoisi:
        MotsEnCours+= "*"

    LettreChoisiBAD= []
    LettreChoisiGOOD = []

    while MotsEnCours != motsChoisi and nombre_de_chance > 0 :

        print("Votre mot est : ", MotsEnCours, "et il ne vous reste que ", nombre_de_chance, " de le trouver...")
        print ("Quelle lettre voulez vous essayer maintenant ?")

        lettre = input(">>")
        
        if lettre == "" or len(lettre) > 1 :
            print("veuillez taper une et une seule lettre merci, bougre :))")
            continue
        
        if lettre in LettreChoisiBAD or lettre in LettreChoisiGOOD:
            print("Vous avez déjà tapé cette lettre petit bougond")
        elif lettre in motsChoisi:
            print("Vous avez trouvé une lettre")
            print(lettre,"  ",motsChoisi)
            LettreChoisiGOOD += lettre
            MotsEnCours = ""
            for tempLettre in motsChoisi :
                
                if tempLettre in LettreChoisiGOOD:
                    MotsEnCours += tempLettre
                else :
                    MotsEnCours += "*"


        else :
            print("et bah....non, cette lettre n'y est pas")
            nombre_de_chance-=1
            LettreChoisiBAD += lettre
            if nombre_de_chance == 0 :
                print("Vous avez perdu désolé....")
            
       

    if MotsEnCours == motsChoisi :
        print("Bravo vous avez gagné!!")
    
    elif nombre_de_chance == 0 :
        print("Vous avez perdu :{")

    print("Voulez vous refaire une partie ? y/n")
    
    answer = input(">>")

    if answer == "y":
        startAgain = True
    else :
        startAgain = False