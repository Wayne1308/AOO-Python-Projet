import unittest
from model.salle import Salle

class TestSalle(unittest.TestCase):
    def test_salle_creation(self):
        salle = Salle("S01", "Conférence", 10)
        self.assertEqual(salle.identifiant, "S01")
        self.assertEqual(salle.type_salle, "Conférence")
        self.assertEqual(salle.capacite, 10)
        self.assertIsNotNone(salle.id)

if __name__ == '__main__':
    unittest.main()
