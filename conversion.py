def convBinaire (nombre):
    if nombre == 0:
        return ""
    
    else:
        return convBinaire(nombre//2) + str(nombre%2)


def affiche(n):
    for i in range (1, n+1):
        print (i, "---->", convBinaire(i))

affiche(100)