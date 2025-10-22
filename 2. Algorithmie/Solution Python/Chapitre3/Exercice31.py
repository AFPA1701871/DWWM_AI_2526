# VARIABLES
nb = None  # Déclaration de la variable 'nb' (sans initialisation)

# Demander un nombre à l'utilisateur
nb = float(input("Entrez un nombre : "))

# Tester si le nombre est positif
if nb > 0:
    # Le nombre est positif
    print("Le nombre est positif")
else:
    # Le nombre est négatif ou nul
    print("Le nombre est négatif")