# VARIABLES
nom1 = None  # Déclaration de la variable 'nom1' (sans initialisation)
nom2 = None  # Déclaration de la variable 'nom2' (sans initialisation)
nom3 = None  # Déclaration de la variable 'nom3' (sans initialisation)

# Demander les 3 prénoms à l'utilisateur
nom1 = input("Entrez le premier prénom : ")
nom2 = input("Entrez le second prénom : ")
nom3 = input("Entrez le troisième prénom : ")

# # Tester si les prénoms sont dans l'ordre alphabétique
# if nom1 < nom2 and nom2 < nom3:
#     # Les prénoms sont dans l'ordre alphabétique
#     print("Ils sont dans l'ordre alphabétique")
# else:
#     # Les prénoms ne sont pas dans l'ordre alphabétique
#     print("Ils ne sont pas dans l'ordre alphabétique")
    
if nom1 < nom2  < nom3:
    # Les prénoms sont dans l'ordre alphabétique
    print("Ils sont dans l'ordre alphabétique")
else:
    # Les prénoms ne sont pas dans l'ordre alphabétique
    print("Ils ne sont pas dans l'ordre alphabétique")
    