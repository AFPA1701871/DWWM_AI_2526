# Demander le premier nombre à l'utilisateur
a = float(input("Entrez le premier nombre : "))

# Demander le second nombre à l'utilisateur
b = float(input("Entrez le second nombre : "))

# Tester si le produit des deux nombres est nul ou positif ou négatif
if a == 0 or b == 0:
    # Le produit des deux nombres est nul
    print("Le produit des deux nombres est nul.")
else:
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        # Le produit des deux nombres est positif
        print("Le produit des deux nombres est positif")
    else:
        # Le produit des deux nombres est négatif
        print("Le produit des deux nombres est négatif")