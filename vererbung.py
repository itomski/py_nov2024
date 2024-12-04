
class Lebewesen():

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def zeige_position(self):
        print(f"{self.__x} {self.__y}")


class Hund(Lebewesen): # Hund IS-A Lebewesen
    
    def __init__(self, rasse, name):
        super().__init__() # Konstruktor der Elternklasse
        self.__rasse = rasse
        self.__name = name

class Katze(Lebewesen): # Katze IS-A Lebewesen
    
    def __init__(self, name):
        super().__init__()  # Konstruktor der Elternklasse
        self.__name = name

h1 = Hund('Dackel', 'Bob')
h1.zeige_position()

class HashText():

    def print(self, text):
        print(f'###{text}###')

class NumText():

    def print(self, text):
        print(f'123{text}123')

class MyText(NumText, HashText):
    pass

text = MyText()
text.print('Das ist das Haus von Nikigraus')