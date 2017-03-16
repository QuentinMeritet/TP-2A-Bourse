from client import Reseau 
import time
r=Reseau() 

num_partie=r.creerPartie('botquentin')
print(num_partie)

top = input("entrer pour top")
r.top()
time.sleep(1)
r.bid('Trydea',3, 100)
r.bid('Facebook',3, 100)
r.bid('Apple',3, 100)
r.bid('Google',3, 100)

r.ask('Trydea',3, 100)
r.ask('Facebook',3, 100)
r.ask('Apple',3, 100)
r.ask('Google',3, 100)


