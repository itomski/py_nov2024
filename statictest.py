
class Fahrzeug():

    ANZ_RAEDER = 4 # Klassen Konstante

    def __init__(self, marke):
        # marke = lokale Variable
        # self.marke = Instanzvariable
        # Namenskonventionen
        # _marke = protected
        # __marke = private
        self._marke = marke

    # Getter
    def get_marke(self):
        return self._marke

    # Setter
    def set_marke(self, marke):
        self._marke = marke

    # Klassenmethode
    @staticmethod
    def show_anz_raeder():
        print(Fahrzeug.ANZ_RAEDER)

    # Klassenmethode
    @classmethod
    def show_anz_raeder2(cls):
        print(cls.ANZ_RAEDER)


f = Fahrzeug('Volvo')
print(f.get_marke())
f.set_marke('Vw')
print(f.get_marke())

print()
f2 = Fahrzeug('Ford')
print(f.get_marke())
print(f2.get_marke())

print(f.ANZ_RAEDER)
print(f2.ANZ_RAEDER)

#f.ANZ_RAEDER = 6 # Definiert eine eigene Instanz-Property
Fahrzeug.ANZ_RAEDER = 6 # Ändert die Property für alle Objekte

print(f.ANZ_RAEDER)
print(f2.ANZ_RAEDER)

#del f.marke # Property wird gelöscht
#del f # Objekt wird gelöscht
#print(f.marke)

#print(Fahrzeug.get_marke()) # hier gibt es kein self, da wir mit der Klasse arbeiten

Fahrzeug.show_anz_raeder() # Aufruf einer statischen Methode
Fahrzeug.show_anz_raeder2() # Aufruf einer statischen Methode