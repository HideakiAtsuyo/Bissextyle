import os
annee = input("Saisissez une année : ")

annee = int(annee)

if annee % 400 == 0 and annee % 4 == 0:
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
os.system("pause")
