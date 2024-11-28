print("Das ist das Haus von \"Nikigraus\"")
print('Das ist das Haus von "Nikigraus"')

zahl = 100 # Bla bla bla
print(zahl)

zahl = '100 Euro'
#print(zahl)

"""Das ist 
Das Haus von
Nikigraus"""

name = 'Peter'

print('Das ist das Haus von ' + name + '.')
print(f'Das ist das Haus von {name}.')

preis = 10.00
print(f'Der Preis ist {preis:.2f} EUR')
#print('Das ist das Haus von \tNikig\nraus')

preis1 = 100;
#preis2 = preis1;
preis2 = 100;

print(preis1)
print(preis2)

preis1 = 200;

print(preis1 is preis2) # Ist es das gleiche Objekt?
print(preis1 == preis2) # Ist es der gleiche Wert?

print()

name1 = "Peter"
name2 = input("Name: ") # List einen String von der Konsole ein

print(name1)
print(name2)
print(name1 is name2) # Ist es das gleiche Objekt?
print(name1 == name2) # Ist es der gleiche Wert?