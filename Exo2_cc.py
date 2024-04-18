# Chaîne de caractères donnée 
chaine = "Python est un langage de programmation puissant et facile à apprendre."

# Extraction simple du mot "Python"
mot_python = chaine.split()[0]  # j'utilise split() pour separer ma chaine en sous chaine,[0] l'index
print("Mot 'Python':", mot_python)

print(chaine[14:39:1]) # je definie ma chaine de caracteres "chaine"

# extraction le mot apprendre en utilisant les indices negatives

print(chaine[-1:-10:-1]) # commence à compter à -1 , je m'arrete à -10 en sautant - 1 à chaque fois

print(chaine[-1::-1])


