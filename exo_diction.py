
def etudiants_avec_bonne_note(etudiants):
    
    
    
    
    etudiants_bons = {}
    for nom, note in etudiants.items():
        if note >= 15:
            etudiants_bons[nom] = note
    return etudiants_bons

# Exemple d'utilisation
etudiants_notes = {
    "Alice": 17,
    "Bob": 14,
    "Charlie": 16,
    "David": 13,
    "Eva": 18
}

etudiants_bons_notes = etudiants_avec_bonne_note(etudiants_notes)
print("Étudiants avec une note moyenne supérieure ou égale à 15 :", etudiants_bons_notes)