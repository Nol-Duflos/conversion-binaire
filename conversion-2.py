print("Entrez le nombre à convertir : ")
nb= input()
nb = int(nb)

resultat = ""

while(nb != 0):
    r = int(nb%2)
    nb = int(nb/2)

    resultat = str(r) + resultat

print("Le chiffre en binaire est : "+ resultat)