
convBinaire = int(input("Entrez le nombre à convertir :"))

resultat = ""


while(convBinaire != 0):
    reste = int(convBinaire%2)
    convBinaire = int(convBinaire/2)

    resultat = str(reste) + resultat

print("Le chiffre en binaire est : "+ resultat)