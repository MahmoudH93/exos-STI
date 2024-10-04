def lpp(a,b):
    if a<b:
        return a
    else:
        return b
print(lpp(2.1,1.3))


def valeur_absolue(x):
    if x<0:
        x=x*-1
    else:
        return x
    return x
print(valeur_absolue(-5))


def est_entier(x):
    if x==int:
        return True
    else:
        return False
print(est_entier(2.8))


def est_pair(n):
    if n%2==0:
        return True
    else:
        return False
print(est_pair(13))


def intervalle1(x):
    if -2<x<=3:
        return True
    else:
        return False
print(intervalle1(1))



def intervalle2(x):
    if x<=-3 or x>=5:
        return True
    else:
        return False
print(intervalle2(1))


def intervalle3(x):
    if -5<x<=-3 or 0<=x<2:
        return True
    else:
        return False
print(intervalle3(667))


def intervalle4(x):
    if x>1:
        return True
    else:
        return False
print(intervalle4(2))


def signe(x):
    if x==0:
        return ("nul")
    if x<0:
        return ("negatif")
    if x>0:
        return ("positif")
print(signe(0))


def est_bissextile(n):
    if n%400==0:
        return (n,"est bissextile")
    if n%100==0:
        return (n,"est pas bissextile")
    if n%4==0:
        return (n,"est bissextile")
print(est_bissextile(2000))


def nb_pairs(n):
    for k in range(n+1):
        print(2*k)
print(nb_pairs(5))


def suite(n):
    u=1
    for i in range(n):
        u=2*u+i
    return u
print(suite(10))


def seuil(eps):
    u=1
    n=0
    while (u>eps):
        u=u/(n+1)
        n=n+1
    return n


def somme_puissance_trois(n):
    S=0
    for j in range(4,n):
        S=S+3**j
    return S
print(somme_puissance_trois(23))


def somme_puissances(n,p):
    for i in range(1,n):
        n=n**p
    return n


def mult_7(n):
    counter=0
    for i in range(1,n+1):
        if i%7==0:
            counter+=1
    return counter
print(mult_7(15))


def mult_7_pas_3_5(n):
    counter=0
    for i in range(1,n+1):
        if i%7==0 and (i%3!=0 and i%5!=0):
            counter+=1
    return counter
print(mult_7_pas_3_5(35))


def est_parfait(n):
    counter=0
    for i in range(1,n+1):
        if n%i==0:
            counter+=i
    return counter == 2*n
print(est_parfait(6))


def factorielle(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact
print(factorielle(6))


def suite_u(n):
    u=4
    for i in range(n):
        u=2-u/2
    return u
print(suite_u(8))


def suite_F(n):
    if n==0:
        return0
    elif n==1:
        return 1
    else:
        F0,F1=0.1
    for i in range(2,n+1):
        Fn=F1+F0
        F0,F1=F1,Fn
    return F1




def f (n):
    n>0
    return n*'c'
print(f (3))


def f (n,m):
    n>0
    m>0
    return n*'c', m*'d'
print(f (3,5))


def f (n):
    n>0
    return n*'ch'
print(f (3))



def sous_chaine (ch1,ch2):
    return ch1 in ch2 or ch2 in ch1


def triple_six(ch):
    return '666' in ch


def triple_six_exact(ch):
    n=len(ch)
    if ch[0:3]== '666' and ch[3]!='6':
        return True
    if ch[n-3:n]== '666' and ch[n-4]!='6':
        return True
    for k in range(1,n-3):
        if ch[k:k+3]=='666' and ch[k-1]!='6' and ch[k+3]!='6':
            return True
        return False


def miroir2(ch):
    inv=''
    for e in ch:
        inv=e+inv
    return inv


def palindrome(ch):
    return ch==ch[::-1]



def affiche4():
    for m in range (4):
        print(m)


L=[]
for k in range(1,101):
    L+=[k]
print(L)


L=[]
for k in range(1,101):
    L.append(k)
print(L)



L=[]
L=100*[0]
for k in range(1,101):
    L[k-1]=k
print(L)

for i in range(len(L)):
    L[i]*=2
print(L)



def carre(n):
    return [i**2 for i in range(1,n+1)]
print(carre(5))


doubles=[2*i for i in range(1,10)]
print(doubles)

def carre_compr(n):
        return [i**2 for i in range(1,n+1)]
print(carre_compr(10))



