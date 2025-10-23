# for i in range(0, 5):
#     print(f"Bonjour {i}")
    
# for _ in range(0, 5):
#     print("Bonjour")

# liste=[1,8,3,4,5]
# for i in range( len(liste)):
#     print(liste[i])

# a=0
# while a<10:
#     a+=1
#     print(a)


# i = 1
# while i < 20:
#     if i==10 :
#         print("anniversaire dizaine")
#         i+=1   # il faut incrementer i pour eviter la c=boucle infinie
#         continue  # arrete ce tour de boucle et repend au while
#     if i==18:
#         print("majeur")
#         break  #arrete completement la boucle
#     print(f"anniversaire {i} ans")
#     i += 1

# Remplir une liste
# liste=[]
# for i in range( 5):
#     nb = int(input("Entrer un nombre : "))
#     # liste[i] = nb
#     liste.append(nb)
# print(liste)

liste=[]
for i in range( 5):
    liste.append(int(input("Entrer un nombre : ")))
print(liste)