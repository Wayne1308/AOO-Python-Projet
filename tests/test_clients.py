import unittest
from model.client import Client

class TestClient(unittest.TestCase):
    def test_client_creation(self):
        client = Client("John", "Doe", "john@example.com")
        self.assertEqual(client.nom, "John")
        self.assertEqual(client.prenom, "Doe")
        self.assertEqual(client.email, "john@example.com")
        self.assertIsNotNone(client.id)

if __name__ == '__main__':
    unittest.main()
