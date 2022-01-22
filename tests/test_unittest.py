import unittest

class Test_TestAPI(unittest.TestCase):

    def test_connexion(self):
        self.assertEqual(404, 404)

    def test_set(self):
        self.assertEqual(200,404)

if __name__ == '__main__':
    unittest.main()