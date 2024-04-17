# le definis une fonction  de chaine de caracteres compter_majuscules_minuscules 

def compter_majuscules_minuscules(chaine):

    nb_majuscules = 0   # je ne dispose pas encore de majuscules
    nb_minuscules = 0   # je ne dispose pas encore de minuscules 
    
    for caractere in chaine:  #  pour tous les caracteres de ma chaine
        if caractere.isupper(): # si le caractére est une majuscule
            nb_majuscules += 1  # compter 1
        elif caractere.islower():# si le caractere est une minuscule
            nb_minuscules += 1   # compter 1 
    
    return nb_majuscules, nb_minuscules # je demande à mon code de me retourner une majuscule ou une minuscule

chaine_utilisateur = input("Entrez une chaîne de caractères : ")
majuscules, minuscules = compter_majuscules_minuscules(chaine_utilisateur)

print("Nombre de majuscules :", majuscules)
print("Nombre de minuscules :", minuscules)
