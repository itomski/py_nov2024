#Aufgabe 3
# Entwerfe eine Sammlung (Modul) an Funktionen für einen Würfelbecher
# Funktionen: 
# Ein Wurf mit einem sechsseitigen Würfel. 
# Das Ergebnis soll als int zurückgegeben werden.

# Ein Wurf mit mehreren sechsseitigen Würfeln. 
# Das Ergebnis soll als eine Int-Liste zurückgegeben werden. 
# Bei Aufruf dieser Funktion wird die gewünschte Anzahl der Würfel als Int-Argument übergeben.

# Auswertung eines Wurfs mit mehreren Würfeln. 
# Hierbei wird das Ergebnis der zweiten Funktion als Argument übergeben. 
# Es folgt eine Konsolen-Ausgabe nach folgendem Schema:
# Wurf-Ergebnis: 
# x mal 1: 
# x mal 2: 
# x mal 3: 
# x mal 
# etc.

import random

def roll():
    return random.randint(1,6)

def roll_more(num):
    #return [roll() for _ in range(num)]
    ergs = []
    for _ in range(num):
        ergs.append(roll())
    return ergs


def stats(val_list): # 3,2 5,1,3
    stats = [0,0,0,0,0,0]
    for val in val_list:
        stats[val - 1] += 1
    i = 1
    for s in stats:
        print(f"{s} mal {i}")
        i += 1

def main():
    print(roll())
    print(roll())
    print(roll())
    print(roll_more(10))
    erg = roll_more(10)
    print(erg)
    print()
    stats(erg)

if __name__ == '__main__':
    main()