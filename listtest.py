namen = [] # leere liste

#for e in range(5):
#    print(e)

for _ in range(5):
    eingabe = input("Eingabe: ");
    if eingabe != 'exit':
        namen.append(eingabe)
    else:
        break # Bricht die Schleife vorzeitig ab

print(namen)
print(namen[0])

list2 = [['Peter', 123], ['Buce', 456]] # 2d Liste

print(list2[1][1])
