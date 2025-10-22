# VARIABLES
heures = None  # Déclaration de la variable 'heures' (sans initialisation)
minutes = None  # Déclaration de la variable 'minutes' (sans initialisation)

# Demander les heures et les minutes à l'utilisateur
heures = int(input("Saisir les heures (0 à 23) : "))
minutes = int(input("Saisir les minutes (0 à 59) : "))

# Calculer les heures et minutes dans une minute
minutes += 1

# Gérer le passage à l'heure suivante si nécessaire
if minutes == 60:
    minutes = 0
    heures += 1
    if heures == 24:
        heures = 0

# Afficher l'heure dans une minute
print(f"Dans une minute, il sera {heures}:{minutes:02d}")