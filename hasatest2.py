
class Scout():

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def friend(self):
        return self.__friend

    @friend.setter
    def friend(self, other):
        self.__friend = other
    
s1 = Scout('Bruce')
s2 = Scout('Carol')

print(s1.name)
print(s2.name)

s1.friend = s2 # Objektbeziehung
s2.friend = s1 # Objektbeziehung

print(f"Freund von {s1.name} ist {s1.friend.name}")
print(f"Freund von {s2.name} ist {s2.friend.name}")