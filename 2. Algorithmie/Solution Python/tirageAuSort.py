from random import randint

liste=["Miguel","Pierre","Antonio","Capucine","Yousri","Antoine","Théo","Léo","Christophe","Guillaume"]
for i in range(len(liste)):
    print(liste.pop(randint(0,len(liste)-1)))
