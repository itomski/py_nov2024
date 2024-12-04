
class Pkw():
    
    def __init__(self, kennzeichen) -> None:
        self.__kennzeichen = kennzeichen

    def __str__(self):
        return self.__kennzeichen + ' ' + str(self.__parkplatz)
    
    def set_parkplatz(self, parkplatz):
        self.__parkplatz = parkplatz

class Parkplatz():
    def __init__(self):
        self.__fahrzeuge = [] # Parkplatz HAS-A PKWs

    def einparken(self, fahrzeug: Pkw):
        self.__fahrzeuge.append(fahrzeug)
        fahrzeug.set_parkplatz(self)

    def zeige_fahrzeuge(self):
        for f in self.__fahrzeuge:
            print(f)

parkplatz = Parkplatz()
parkplatz.einparken(Pkw('HH:AB123'))
parkplatz.einparken(Pkw('HB:CD227'))
parkplatz.einparken(Pkw('B:ZZ172'))

parkplatz.zeige_fahrzeuge()