
# VARIABLES
prixht = None  # Déclaration de la variable 'prixht' (sans initialisation)
tva = None  # Déclaration de la variable 'tva' (sans initialisation)
nb = None  # Déclaration de la variable 'nb' (sans initialisation)
prixttc = None  # Déclaration de la variable 'prixttc' (sans initialisation)

# Demander le prix hors taxe à l'utilisateur
prixht = float(input("Entrez le prix hors taxe : "))

# Demander le nombre d'articles à l'utilisateur
nb = int(input("Entrez le nombre d'articles : "))

# Demander le taux de TVA à l'utilisateur
tva = float(input("Entrez le taux de TVA : "))

# Calculer le prix TTC
prixttc = nb * prixht * (1 + tva)

# Afficher le prix TTC
print(f"Le prix TTC est : {prixttc} ")