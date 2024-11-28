
name = input("Name: ")
print(f"Hallo {name}")

alter = int(input('Wie alt bist du? ')) # String in int konvertieren
alter += 4 # alter = alter + 4
print(f"In vier Jahren bist du {alter}")

print(type(name))
print(type(alter))
print(float(alter)) # Konvertierung von int in float
print(str(alter)) # Konvertierung von int in string
print(bool(alter)) # Konvertierung von int in boolean

# komplexe Zahl
#zahl = 10j
#print(type(zahl))