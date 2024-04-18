def est_palindrome(mot):
    
    
    
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    
    
    # j'etablis un compteur pour compter le nombre de mot palindromique
    compte = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            compte += 1
    return compte


liste_mots = ["pikatchu", "mamadou", "amadou", "poundou", "bambou"]
nombre_palindromes = compter_palindromes(liste_mots)

print("La liste contient", nombre_palindromes, "palindromes.")