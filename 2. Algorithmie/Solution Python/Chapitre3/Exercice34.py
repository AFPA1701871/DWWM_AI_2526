# VARIABLES
nombre = None  # Déclaration de la variable 'nombre' (sans initialisation)

# Demander un nombre à l'utilisateur
nombre = float(input("Saisir un nombre : "))

# Tester si le nombre est nul, négatif ou positif
if nombre == 0:
    # Le nombre est nul
    print("Le nombre est nul.")
elif nombre < 0:
    # Le nombre est négatif
    print("Le nombre est négatif")
else:
    # Le nombre est positif
    print("Le nombre est positif")