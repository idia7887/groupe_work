def calcul_2(chaine_a_traiter):
    #initialiser a 0 maj et min
    numb_maj = 0
    numb_min = 0
    for e in chaine_a_traiter:
        if e.isupper():  #je parcours mon tableau pour identifier les elements maj
            numb_maj +=1
            
        elif e.islower(): # on fait un elif ici pour eviter que d'autre
            numb_min +=1 #caractere soit considere comme mini pourquoi? parce que j'allais faire sinon = mini 
    return numb_min,numb_maj
    

# je veux parcourirs ma chaine, je stock le imput dans un tableau
##chaine_a_traiter =[]
chaine_a_traiter= input("quel est votre chaine de caractere?")
numb_miniscule,numb_majuscule = calcul_2(chaine_a_traiter)
#compte=calcul_2(chaine_a_traiter)
print("Nombre de majuscule :", numb_majuscule) #ici je print un msg qui affichera le nombr de maj
print("Nombre de Miniscule :", numb_miniscule)
#choix=input("voulez vous continuer Y/N")



