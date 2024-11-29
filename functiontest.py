
#add(10, 20) # Error: Hier ist die Funktion noch nicht bekannt

def add(a = 0, b = 0):
    print(a + b)

def multi(a, b):
    return a * b

#def add(a, b):
#    print(a - b)

add(10, 15)
add(1, 7)
add(99, 1)
add(99)
add()
# add(99) # Error: der zweite Parameter fehlt

erg = multi(99, 2)
print(erg)
print(multi(99, 2))