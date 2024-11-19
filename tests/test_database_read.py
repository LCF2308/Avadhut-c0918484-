import unittest
import sys 
import os
from pymongo.errors import ConnectionFailure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import  app,db

class TestDatabaseRead(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """This method will run once for the entire test class."""
        # Ensure the app is connected to the database
        try:
            # Try to ping the MongoDB database to check the connection
            db.client.admin.command('ping')  # Use 'ping' to check if the database is reachable
            cls.db_connected = True
        except ConnectionFailure:
            cls.db_connected = False

    def test_ping_database(self):
        """Test if the database connection is successful."""
        self.assertTrue(self.db_connected, "Failed to connect to the MongoDB database")

    def test_read_operation(self):
        """Test MongoDB read operation."""
        # Test if we can fetch data from the 'products' collection
        products = db.products.find()
        self.assertIsNotNone(products, "Failed to fetch data from 'products' collection")
        self.assertGreater(len(list(products)), 0, "No products found in the database")

if __name__ == "__main__":
    unittest.main()
