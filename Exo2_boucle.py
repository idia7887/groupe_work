def show_pyramid(height):
    for i in range(height):   
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Demander à l'utilisateur la hauteur de la pyramide
height = int(input("Enter the height of the pyramide : "))

# Afficher la pyramide
show_pyramid(height) 



