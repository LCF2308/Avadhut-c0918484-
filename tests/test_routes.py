import unittest
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app  # Import the Flask app

class RouteTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client"""
        self.client = app.test_client()

    def test_invalid_method(self):
        """Test that sending a POST request to a GET-only route returns a 405 error"""
        # Send a POST request to the /products route, which only accepts GET requests
        response = self.client.post('/products')
        self.assertEqual(response.status_code, 405)  # Expect a 405 error for invalid method

if __name__ == '__main__':
    unittest.main()
