# VARIABLES
heures = None  # Déclaration de la variable 'heures' (sans initialisation)
minutes = None  # Déclaration de la variable 'minutes' (sans initialisation)
secondes = None  # Déclaration de la variable 'secondes' (sans initialisation)

# Demander les heures, minutes et secondes à l'utilisateur
heures = int(input("Saisir les heures (0 à 23) : "))
minutes = int(input("Saisir les minutes (0 à 59) : "))
secondes = int(input("Saisir les secondes (0 à 59) : "))

# Incrémenter les secondes d'une unité
secondes += 1

# Gérer le passage à la minute suivante si nécessaire
if secondes == 60:
    secondes = 0
    minutes += 1
    # Gérer le passage à l'heure suivante si nécessaire
    if minutes == 60:
        minutes = 0
        heures += 1
        # Gérer le passage au jour suivant si nécessaire
        if heures == 24:
            heures = 0

# Afficher l'heure dans une seconde
print(f"Dans une seconde, il sera {heures}:{minutes:02d}:{secondes:02d}")