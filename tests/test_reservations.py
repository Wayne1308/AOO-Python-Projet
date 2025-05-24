import unittest
from model.reservation import Reservation

class TestReservation(unittest.TestCase):
    def test_reservation_creation(self):
        r = Reservation("client123", "salle456", "2025-05-23 10:00", "2025-05-23 12:00")
        self.assertEqual(r.client_id, "client123")
        self.assertEqual(r.salle_id, "salle456")
        self.assertEqual(r.date_debut, "2025-05-23 10:00")
        self.assertEqual(r.date_fin, "2025-05-23 12:00")
        self.assertIsNotNone(r.id)

if __name__ == '__main__':
    unittest.main()
