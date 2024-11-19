import unittest
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestDatabaseWrite(unittest.TestCase):

    def setUp(self):
        """This method runs before every test case."""
        # Set up a clean environment before each test (e.g., clear the 'products' collection).
        db.products.delete_many({})  # Clear any previous data in 'products' collection

    def test_write_operation(self):
        """Test MongoDB write operation."""
        new_product = {
            "name": "Test Product",
            "tag": "Test Tag",
            "price": 100.0
        }

        # Insert the new product into the 'products' collection
        result = db.products.insert_one(new_product)

        # Check if the product was inserted successfully
        self.assertIsNotNone(result.inserted_id, "Failed to insert document into MongoDB")

        # Verify the product is present in the database
        inserted_product = db.products.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_product, "Inserted product not found in the database")
        self.assertEqual(inserted_product['name'], new_product['name'], "Product name does not match")
        self.assertEqual(inserted_product['tag'], new_product['tag'], "Product tag does not match")
        self.assertEqual(inserted_product['price'], new_product['price'], "Product price does not match")

if __name__ == "__main__":
    unittest.main()
