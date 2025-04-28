argent=float(input("Combien d'argent veut tu mettre dans la banque ?"))
taux=float(input("Quel est le taux d'intérêt ?"))
time=int(input("Tu vas laisser l'argent combien de temps ?"))

for i in range(time):
    argent= (1+taux/100)*argent

print("Tu auras",argent, "euros")