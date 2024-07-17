from random import *

nekibr = randrange(1, 100)
pokusaj = -1
brojpok = 0
while (pokusaj!=nekibr):
    pokusaj= int(input("Zamisljeni broj je(1-100): "))
    brojpok +=1
    if pokusaj > nekibr:
        print ("Probajte manji broj!")
    elif pokusaj < nekibr:
        print ("Pokusajte neki veci broj!")
        

print ("Nakon ", brojpok, "pokusaja ste pogodili broj")    
