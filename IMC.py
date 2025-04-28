poids = float(input("Quel est ton poids (en kg) ?"))
taille = float(input("Quelle est ta taille (en m) ?"))
IMC = poids/(taille*taille)
if IMC>30 :
    print("Tu dois te mettre au régime")
else :
    print("Tu n'as pas besoin de te mettre au régime")