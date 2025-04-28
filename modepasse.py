mdp="Skibiditoilet75"

nberreur= 0

while nberreur<2 :
    essai=input("Donne le mot de passe bruzz")
    if essai==mdp :
        print("bravissimo c le modepasse")
        break
    else :
        print("reessaye mgl")
        nberreur += 1
if nberreur==2 :
    print("bztm t'as plus d'essais")
