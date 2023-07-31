import random
import os
import time
import sys

def tura_komputera():
    wybor_komputera=random.randrange(1,4)
    return wybor_komputera


def tura_gracza():
    print("1. Kamien \U0001F5FF 2. Papier \U0001F4DC 3. Nozyce \U00002702")
    wybor_gracza=int(input("Wybierz kamien, papier albo nozyce(wpisz 1-3): "))
    return wybor_gracza


def ikonki(wybor):
    if wybor==1:
        return "\U0001F5FF" #kamien
    elif wybor==2:
        return "\U0001F4DC" #papier
    else:
        return "\U00002702" #nozyce 


punkty_gracza=0
punkty_komputera=0


def punktacja(wygrana_gracza,wygrana_komputera):
    global punkty_gracza,punkty_komputera
    if wygrana_gracza:
        punkty_gracza+=1
    elif wygrana_komputera:
        punkty_komputera+=1

def gra(rundy):
    i=0
    wygrane = {1: 2, 2: 3, 3: 1}
    
    while i<rundy:
        os.system('cls')
        print("Runda "+str(i+1)+" z "+str(rundy))
        
        wybor_komputera = tura_komputera()
        wybor_gracza = tura_gracza()

        if wybor_komputera == wybor_gracza:
            print("Jest remis, runda zostanie powtorzona")
            
        elif wybor_gracza == wygrane[wybor_komputera]:
            print("Gracz wygral. " + ikonki(wybor_gracza) + " pokonuje " + ikonki(wybor_komputera))
            punktacja(wygrana_gracza=True, wygrana_komputera=False)
            i+=1
            
        else:
            print("Komputer wygral. " + ikonki(wybor_gracza) + " przegrywa z " + ikonki(wybor_komputera))
            punktacja(wygrana_gracza=False, wygrana_komputera=True)
            i+=1
            
            
        czas=0
        print("\nKolejna runda rozpocznie sie za 3 sekundy",end="")
        while czas<3:
            print(".",end="")
            czas+=1
            sys.stdout.flush()
            time.sleep(1)
            
        print()
            
        
        
rundy=int(input("Ile rund ma miec gra?:"))
gra(rundy)

print("\n PODSUMOWANIE")

if punkty_gracza>punkty_komputera:
    print("Gre wygral GRACZ")
else:
    print("Gre wygral KOMPUTER")
    
print("Komputer: "+str(punkty_komputera))
print("Gracz: "+str(punkty_gracza))