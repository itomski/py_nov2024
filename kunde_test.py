import unittest
from ooptest2 import Kunde

class TestKunde(unittest.TestCase):

    # Testet, ob die Methode der Klasse richtig funktioniert
    def test_get_info(self):
        k = Kunde('Peter')
        dict = k.get_info()
        self.assertEqual(dict['vorname'], 'Peter', 'Vorname passt nicht')
        self.assertEqual(dict['nachname'], 'Parker', 'Nachname passt nicht')

if __name__ == '__main__':
    unittest.main()