# Zwei Klassen:
# "Buch" mit dem Attribut "titel" (public get)
# "Autor" mit dem Attribut "name" (public get)
# jeweils einen Konstruktor, der die Eigenschaften initialisiert.
# Implementieren Sie die Assoziation der beiden Klassen und stellen Sie eine bidirektionale Navigierbarkeit her.
# Dazu müssen Sie den Klassen weitere Member hinzufügen.
# (Gehen Sie davon aus, dass ein Buch mehrere Autoren haben und ein Autor mehrere Bücher verfassen kann)
# Testen Sie das Programm im Main.

class Book:
    def __init__(self, title, authors):
        self.__title = title
        self.__authors = authors

        a: Author  # Typ-Hinweis
        for a in authors:
            a.get_books().append(self)

    def get_title(self):
        return self.__title

    def set_authors(self, authors):
        self.__authors = authors

    def get_authors(self):
        return self.__authors

    def __str__(self):
        string = "Title: " + self.__title + "\n" + "Authors: \n"
        for a in self.__authors:
            string += str(a) + "\n"
        return string


class Author:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def get_name(self):
        return self.__name

    def set_books(self, books):
        self.__books = books

    def get_books(self):
        return self.__books

    def __str__(self):
        return "Name: " + self.__name


a1 = Author("William Gibson")
a2 = Author("Bruce Sterling")
a3 = Author("Stanislaw Lem")

b1 = Book("Idoru", [a1])
b2 = Book("Solaris", [a3])
b3 = Book("Die Differenzmaschine", [a1, a2])

# Ausgabe aller Books der jeweiligen Authors
for b in a1.get_books():
    print(b)

for b in a2.get_books():
    print(b)

for b in a3.get_books():
    print(b)