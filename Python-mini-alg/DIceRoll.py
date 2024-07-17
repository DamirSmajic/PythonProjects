import emoji
from random import * 

# Definicija potrebnih varijabli 
n = 0
brojacIstih = 0
bacanja = ()

while n<3 or n>5:
    n = int(input("Unesite zeljenji broj bacanja (3 - 5): "))

def bacanjeKocke(n, brojacIstih, bacanja):
    for i in range(n):
        bacanja += (randrange(1, 7),)
    print (bacanja)
    for j in range(len(bacanja)):
        if brojacIstih < 3:
            brojacIstih = 0
        for k in range(len(bacanja)):
            if bacanja[j] == bacanja[k]:
                brojacIstih += 1
        
    if brojacIstih >= 3:
        print ("WOW od", n, "bacanja", emoji.emojize(':game_die:'), "imali ste 3 ili vise istih brojeva", emoji.emojize(':smile:'))
    else:
        print ("Od", n, "bacanja imali ste manje od 3 ista broja", emoji.emojize(':rage:')) 


bacanjeKocke(n, brojacIstih, bacanja)
