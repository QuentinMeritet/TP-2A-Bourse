from client import Reseau
import time

r=Reseau()

######## fonctions ########



def creation_partie():
    num_partie=r.creerPartie("Latermcdelo")  #creation partie
    print(num_partie)   #numero du joueur


def rejoindre_partie(numero,nom):
    r.rejoindrePartie(numero,'nom')
    r.top()

def achats():
    facebook = r.achats('Facebook')
    trydia = r.achats('Trydia')
    google = r.achats('Google')
    apple = r.achats('Apple')
    print("facebook :  ",facebook)
    print("trydia :  ",trydia)
    print("google :  ",google)
    print("appl :  ",apple)





def partie():
    from client import Reseau
    r=Reseau()
    print("rejoindre partie=0  creer partie=1")
    test=input("0 ou 1\n")
    test=int(test)

    if test==0:
        numero = int(input("numero de la partie:  "))
        rejoindre_partie(numero,"latermocdelo")
    elif test==1:
        creation_partie()
        temps= input("temps d'attente ? en seconde\n")
        time.sleep(temps)
        r.top()
    while True :
        entree=input("que faire ?\n s:solde\n a:ask\n b:bid\n")
        if entree=="s":
            print(r.solde())
        if entree=="a":
            action = input("action ?\n")
            prix = input("prix?\n")
            volume = input("volume ?\n")
            r.ask(action,prix,volume)
        if entree == "b":
            action = input("action ?\n")
            prix = input("prix?\n")
            volume = input("volume ?\n")
            r.bid(action, prix, volume)



########### Code ##########

partie()
