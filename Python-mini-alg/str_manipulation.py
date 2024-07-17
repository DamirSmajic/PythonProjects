def sortiramString (string):
    """ (str) -> str
    Primljeni string sortira abecedno. Vraca sortiran string.
    >>> sortiram_string ('mala ulica')
     aaacillmu
    """
    lista = list(string)
    lista.sort()
    return ''.join(lista)

def invertujem_rijeci (string):
    """ (str) -> str
    Funkcija invertuje rijeci primljenog stringa u vraca novi string sastavljen od invertovanih rijeci
    >>> invertujem_riojeci('mala ulica')
    alam acilu
    """
    lists_str = string.split()
    for i in lists_str:
        i = i[::-1]
        print(i, end = ' ')
    

#Zadatak 4

s = input("Unesite neki string: ")
n = int(input("Unesite broj slova koje ce postati VELIKA!!! : "))

def bogFunkc (s, n):
    """ (str) -> str
    Funkcija prima string, te na osnovu unesenog broja pretvara velika mala slova u velika
    >>> velika_slova('ja sam studentica.', 5)​
    'JA SAm studentica.'
    """
    lista = []
    for i in range(len(s)):
        if (i < n):
            lista.append(s[i].upper())
        else:
            lista.append(s[i])

    s = ''.join(lista)
    print()    
    print (s)
   
#test kod
a = "mala ulica"
print(sortiramString(a))
invertujem_rijeci(a)
bogFunkc(s, n)

