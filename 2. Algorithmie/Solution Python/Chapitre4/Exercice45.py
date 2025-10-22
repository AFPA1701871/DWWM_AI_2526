# VARIABLES
age = None  # Déclaration de la variable 'age' (sans initialisation)
genre = None  # Déclaration de la variable 'genre' (sans initialisation)

# Demander l'âge et le genre à l'utilisateur
age = int(input("Entrez votre age : "))
genre = input("Entrez votre genre (H, F et A) : ").upper()  # Conversion du genre en majuscule

# Déterminer si la personne est imposable
if (genre == "H" and age > 20) or (genre == "F" and 18 < age < 35):
    print("Imposable")
else:
    print("Non imposable")
