import os
annee = int(input("Saisissez une année : "))

if annee % 400 == 0:
    print("L'année saisie est bissextile.\n")
else:
    print("L'année saisie n'est pas bissextile.\n")
os.system("pause")
