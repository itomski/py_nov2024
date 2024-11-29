liste1 = ['Peter', 'Bruce', 'Natasha', 'Carol']
liste2 = liste1 # beide Variablen zeigen auf das Gleiche List-Objekt
liste3 = liste1.copy() # liste3 zeigt auf ein eigenes List-Objekt
liste2.pop()
print(liste1)
print(liste3)

print()

einkauf = []
for _ in range(3):
    einkauf.append([input('Bezeichnung: '), False])

print(einkauf)

for e1 in einkauf:
    for e2 in e1:
        print(e2)

print()

einkauf[2][1] = True

for e in einkauf:
    if(e[1] == False):
        print(f"{e[0]}")