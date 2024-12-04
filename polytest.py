from multipledispatch import dispatch


class Document():

    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content
    
class WordDocument(Document):

    def __init__(self, content):
        super().__init__(content)

    def get_content(self): # Methode wird überschrieben
        return super().get_content() + "... als Word Dokument"
    
class JsonDocument(Document):

    def __init__(self, content):
        super().__init__(content)

    def get_content(self): # Methode wird überschrieben
        return super().get_content() + "... als Json Dokument"


class Printer():

    def print_text(self, doc: Document):
        print(doc.get_content())


    
printer = Printer()
#doc = Document('Das ist das Haus von Nikigraus')
#doc = WordDocument('Das ist das Haus von Nikigraus')
doc = JsonDocument('Das ist das Haus von Nikigraus')
printer.print_text(doc)

print()

docs = []
docs.append(WordDocument('Bla bla bla'))
docs.append(WordDocument('Nix da!'))
docs.append(JsonDocument('...'))
docs.append(Document('######'))
docs.append(JsonDocument('Ganz viele Daten'))
#docs.append("Hallo Welt")

for d in docs:
    printer.print_text(d)

@dispatch(int, int)
def func(a, b):
    print(a + b)

@dispatch(int, int, int)
def func(a, b, c): #Überladen von Funktionen
    print(a - b - c)

func(1, 2)
func(1, 2, 4)