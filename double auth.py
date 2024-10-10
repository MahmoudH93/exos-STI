import random

a = 'le mdp'
mdp = input('Entrez votre mdp : ')
counter = 0

while mdp != a and counter < 2:
    mdp = input('mdp incorrect, veuillez réessayer : ')
    counter += 1

if mdp == a and counter==2:
    code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    with open('code2.txt', 'a') as fichier:
        fichier.write(f'Le code de confirmation est : {code}\n')
    c = input('Entrez le code de confirmation reçu par mail : ')
    if c == code:
        print('Bienvenue !')
    else:
        c2=input('Code incorrect, veuillez reéssayer : ')
    if c2 == code:
        print('Bienvenue !')

elif mdp!=a and counter==2:
    print('Nombre de tentatives dépassé !')
