def intersection(ensemble1, ensemble2):
    # Utilisation de l'opérateur "&" pour trouver l'intersection
    intersection = ensemble1 & ensemble2
    return intersection

# Exemple d'utilisation
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}
resultat = intersection(ensemble1, ensemble2)
print("Intersection des ensembles :", resultat)
