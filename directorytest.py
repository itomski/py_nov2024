
einwohner = {
    "hamburg": 1900000,
    "kiel": 300000,
    "berlin": 3500000,
    "münchen": 1700000
}

einwohner['leipzig'] = 800000 # neuer Eintrag
einwohner['kiel'] = 320000 # update

print(einwohner)

print()

for k in einwohner.keys():
    print(k)

print()

for v in einwohner.values():
    print(v)

print()

for e in einwohner:
    #print(e)
    print(f"{e}: {einwohner[e]}")
