
def main():
    mein_text = 'Hallo Welt'

    def check_length(text):
        return len(text) > 0 and len(text) < 20

    print(check_length(mein_text))
    print(check_length(''))
    print(check_length('Das ist das Haus von Nikigraus!'))

    # Objekterzeugung = Instanzierung
    p = Person()
    print(p)
    print(p.vorname + ' ' + p.nachname)
    print(f"{p.vorname} {p.nachname}") # public Eigenschften lesen
    p.vorname = 'Bla bla bla' # public Eigenschften ändern
    print(f"{p.vorname} {p.nachname}")

    print()
    p1 = Person()
    p2 = Person()
    p2.vorname = 'Bruce'
    print(p1)
    print(p2)

    print()
    p3 = NextPerson('Scott', 'Lang')
    print(p3)
    p3.sag_hallo()

    p3 = NextPerson('Scott')
    print(p3)
    p3 = NextPerson()
    print(p3)
    # print(p3.vorname) # Error, Eigenschaft nicht verfügbar

    print(p3.__dict__) # Erzeugt aus dem Objekt ein Dictionary


# snake_case, Kleinbuchstaben und Unterstriche (Variablen, Funktionen, Methoden)
# SCREAMING_SNAKE_CASE, Großbuchstaben und Unterstriche (KONSTANTEN)
# PascaleCase, beginnt mit Großbuchstaben und jedes Wort beginnt wieder Groß (Klassen)
# camelCase, beginnt mit Kleinbuchstaben und jedes Wort beginnt wieder Groß (wird in Python nicht verwendet)

# Definition einer Klasse
class Person():

    # public Instanz-Eigenschaften. jedes Objekt hat seine eigenen
    # public = jeder darf nach Wunsch lesen und schreiben
    vorname = 'Peter'
    nachname = 'Parker'

    def __str__(self) -> str: # Rückgabetyp str
        return f"Person: {self.vorname} {self.nachname}" # Methode nutzt die Instanzeigenschaften

class NextPerson():

    # Konstruktor
    def __init__(self, vorname = 'Unbekannt', nachname = 'Unbekannt') -> None:
        self.__vorname = vorname # private Instanzeigenschaft
        self.__nachname = nachname
    
    def __str__(self) -> str: # Rückgabetyp str
        return f"NextPerson: {self.__vorname} {self.__nachname}" # Methode nutzt die privaten Instanzeigenschaften
    
    def sag_hallo(self): # Instanz-Methode
        print(f"Hallo! \nMein Name ist {self.__vorname} {self.__nachname}!")


# Eingangstyp str
def mach_was(text: str) -> None: # Rückgabetyp None == void
    print('Hi')

if __name__ == '__main__':
    main()