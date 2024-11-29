
zahl = int(input('Auswahl: '))

# seit Python 3.10
match zahl:
    case 1:
        print("C1")
    case 2:
        print("C2")
    case 3:
        print("C3")
    case 4:
        print("C4")
    case _:
        print("default")


def switch(zahl):
    if zahl == 1:
        print("C1")
    elif zahl == 2:
        print("C2")
    else:
        print("default")    

switch(zahl)