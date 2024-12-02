
zahl1 = 10
zahl2 = 1

def check(val):
    if val < 0:
        raise ValueError('Wert ist zu klein!')
    elif val > 100:
        return False
    else:
        return True


try:
    if check(zahl1) == False:
        zahl1 = 10

    erg = zahl1 / zahl2

except ZeroDivisionError: # ZeroDivisionError einfangen
    print('Problem bei Teilung durch 0')
except ValueError: # ValueError einfangen
    print('Wert ist unter 0')
except: # Alle Exceptions einfangen
    print('Problem')
else:
      print('Wird nur ausgeführt, wenn keine Exception geworfen wurde')  
finally:
    print('Wird immer ausgeführt')


