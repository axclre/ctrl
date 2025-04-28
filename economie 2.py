economie = float(input("Quel est le montant de tes économies ? "))
depense = float(input("Quelle somme estimes-tu dépenser par semaine ? "))
semaine = 0

while economie > 0:
    economie -= depense 
    if economie >= 0:
        semaine += 1

print("Tu peux tenir", semaine, "semaines.")