
class Kunde():
    """Enthät die Daten eines Kunden"""
    def __init__(self, vorname = '', nachname = '') -> None:
        self.__vorname = vorname
        self.__nachname = nachname

    @property
    def vorname(self): # Getter: Lesender Zugriff möglich
        return self.__vorname
    
    @vorname.setter
    def vorname(self, value): # Setter: Schreibender Zugriff möglich
        if len(value) > 0:
            self.__vorname = value
    
    @property
    def nachname(self):
        return self.__nachname
    
    @nachname.setter
    def nachname(self, value):
        if len(value) > 0:
            self.__nachname = value

    def get_info(self):
        return {"vorname": self.__vorname, "nachname": self.__nachname}
    
def einstieg():
    k1 = Kunde('Peter', 'Parker')
    print(k1.vorname + ' ' + k1.nachname)
    k1.vorname = 'Max' # Setter wird benutzt
    k1.nachname = 'Mustermann'
    print(k1.vorname + ' ' + k1.nachname)
    k1.vorname = ''
    print(k1.vorname + ' ' + k1.nachname)
    print(k1.get_info()['nachname'])

if __name__ == '__main__':
    einstieg()