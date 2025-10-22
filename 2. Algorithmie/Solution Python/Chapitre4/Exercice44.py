# VARIABLES
nb = None  # Déclaration de la variable 'nb' (sans initialisation)
prix = None  # Déclaration de la variable 'prix' (sans initialisation)

# Demander le nombre de photocopies à l'utilisateur
nb = int(input("Nombre de photocopies : "))

# Calculer le prix en fonction du nombre de photocopies
if nb <= 10:
    prix = nb * 0.1  # Tarif pour les 10 premières photocopies
elif nb <= 30:
    prix = 10 * 0.1 + (nb - 10) * 0.09  # Tarif pour les photocopies de 11 à 30
else:
    prix = 10 * 0.1 + 20 * 0.09 + (nb - 30) * 0.08  # Tarif pour les photocopies au-delà de 30

# Afficher le montant de la facture
print(f"La facture est de : {prix:.2f}")  # Affichage du prix avec deux chiffres après la virgule
