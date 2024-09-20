from random import randint

def plus_ou_moins():
    nb_mystere=randint(1,100)
    counter=1
    nb_test=int(input("Proposez un nombre entre 1 et 100 :"))
    print("Nombre d essai : ", counter)
    while nb_mystere!=nb_test and counter<7:
        counter=counter+1
        if nb_mystere>nb_test:
            nb_test=int(input("Trop petit ! Testez encore :"))
            print("Nombre d essai : ", counter)
        else :
            nb_test=int(input("Trop grand ! Testez encore :"))
            print("Nombre d essai : ", counter)
    
    if nb_mystere==nb_test:
        print("Bravo ! Le nombre était : ", nb_mystere)
        print("Nombre d essai : ", counter)
    else:
        print("Perdu ! Le nombre était :", nb_mystere)

plus_ou_moins()