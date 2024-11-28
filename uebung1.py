import random

# Erzeuge eine Zufallszahl zwischen 1 und 6
# Der Benutzer hat 3 Versuche die Zahl durch Eigabe zu erraten

zahl = random.randrange(6) + 1;

if int(input("Zahl: ")) == zahl:
    print("Treffer!")
    exit()
else:
    print("Kein Treffer!")

if int(input("Zahl: ")) == zahl:
    print("Treffer!")
    exit()
else:
    print("Kein Treffer!") 


if int(input("Zahl: ")) == zahl:
    print("Treffer!")
    exit()
else:
    print("Kein Treffer!")

print("Ende des Programms!")