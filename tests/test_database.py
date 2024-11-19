import unittest
from pymongo import MongoClient
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client and MongoDB connection"""
        self.client = app.test_client()
        self.db_client = MongoClient(
            'mongodb+srv://<username>:<password>@shopdatabase.up5n2.mongodb.net/shop_db?retryWrites=true&w=majority'
        )
        self.db = self.db_client.shop_db

    def test_mongo_ping(self):
        """Test MongoDB connection using the ping command"""
        try:
            # Try pinging the MongoDB database
            self.db.command('ping')
            is_connected = True
        except Exception as e:
            is_connected = False
        
        self.assertTrue(is_connected, "Failed to connect to MongoDB")

if __name__ == '__main__':
    unittest.main()
