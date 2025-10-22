# VARIABLES
tutu = None  # Déclaration de la variable 'tutu' (sans initialisation)
toto = None  # Déclaration de la variable 'toto' (sans initialisation)
tata = None  # Déclaration de la variable 'tata' (sans initialisation)

# Demander les valeurs de Tutu et Toto à l'utilisateur
tutu = float(input("Indiquez la valeur de Tutu : "))
toto = float(input("Indiquez la valeur de Toto : "))

# Demander la confirmation pour Tata
tata = input("Indiquez la confirmation Ok pour Tata : ").lower()  # Conversion en minuscule

# Déterminer la nouvelle valeur de Tutu
if (tutu <= toto + 4) and (tata != "ok"):
    tutu -= 1  # Diminuer Tutu de 1
else:
    tutu += 1  # Augmenter Tutu de 1

# Afficher la nouvelle valeur de Tutu
print(f"La nouvelle valeur de Tutu est : {tutu}")