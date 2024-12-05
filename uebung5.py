# Erstellen Sie die Klasse "Song" mit den Attributen
# string "Titel", int "DauerSekunden", string "Interpret"
# und der Methode "Spielen", die auf der Konsole alle Informationen über den Song ausgibt
# (die Dauer dabei in Minuten und Sekunden, z.B. 03:35).
# Die Attribute sollen private sein mit öffentlichen Gettern als Eigenschaft, aber keine Setter.
# Über einen Konstruktor sollen die Attribute initialisiert werden.
#
# Erstellen Sie in der Main einen Song und rufen Sie die Methode auf.

class Song:
    def __init__(self, titel, dauer_sekunden, interpret): # Konstruktor
        self.__titel = titel
        self.__dauer_sekunden = dauer_sekunden
        self.__interpret = interpret

    def spielen(self):
        titel = self.__titel
        dauer_minuten = int(self.__dauer_sekunden / 60) # Nachkommastelle entfernen
        dauer_sekunden_rest = self.__dauer_sekunden % 60
        interpret = self.__interpret
        #return "Titel: " + titel \
        #       + " Dauer: " + str(dauer_minuten).zfill(2) + ":" + str(dauer_sekunden_rest).zfill(2) \
        #       + " Interpret: " + interpret

        return f"Titel: {titel} \nDauer: {dauer_minuten:02d}:{dauer_sekunden_rest:02d} \nInterpret: {interpret}"


    def get_titel(self):
        return self.__titel

    def get_dauer_sekunden(self):
        return self.__dauer_sekunden

    def get_interpret(self):
        return self.__interpret


song1 = Song("Neon", 259, "Amplifire")
print(song1.spielen())