
def inverser_tuples(liste_tuples):
    # Créer une liste pour stocker les tuples inversés
    tuples_inverses = []
    
    # Parcourir chaque tuple dans la liste
    for tup in liste_tuples:
        # Inverser l'ordre des éléments dans le tuple et l'ajouter à la liste
        tuple_inverse = tuple(reversed(tup))
        tuples_inverses.append(tuple_inverse)
    
    return tuples_inverses

# Exemple d'utilisation
liste_de_tuples = [(1, 4), (3, 5), (7, 6)]
resultat = inverser_tuples(liste_de_tuples)
print(resultat)  # Affiche : [(2, 1), (4, 3), (6, 5)]


