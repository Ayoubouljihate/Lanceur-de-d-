import random
print("1: Lancer le dé 0:Quitter")
while True:
    # On demande à l'utilisateur de saisir un nombre
    i=int(input("cliquer sur le bouton "))
    if i==0:
        print('Salut')
        break
    elif i==1:
        print(random.randint(1,21))
    else:
        print("Je ne comprend pas")