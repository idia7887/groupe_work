import random

def guess_mystry_num():
    mystry_num = random.randint(1, 50)
    num_trials = 4  # Nomber of authorized trials
    trials = 0

    print("Guess the mystery number between 1 et 50. You have", num_trials, " trials.")

    while trials < num_trials:
        guess = int(input("Enter your guess : "))
        trials += 1

        if guess < mystry_num:
            print("The mystery number is bigger.")
        if guess > mystry_num:
            print("The mystery number is smaller.")
        elif guess == mystry_num:
            print("Congratulations ! You have guess the mestry number in ", trials, "trials.")
        else:
            print("Sorry, you have not guess the mystery number. The mystery number is :", mystry_num)

# Appel de la fonction pour jouer au jeu

guess_mystry_num()