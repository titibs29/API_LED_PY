import unittest
import http.client


class Test_TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.conn = http.client.HTTPConnection("localhost:3000")

    def test_connexion(self):
        self.conn.request("GET", "/")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_control(self):
        self.conn.request("GET", "/control")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_setWrongPin(self):
        self.conn.request("GET", "/set/14/0")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 404)

    def test_setWrongState(self):
        self.conn.request("GET", "/set/11/2")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 400)

    def test_set(self):
        self.conn.request("GET", "/set/11/1")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

        self.conn.request("GET", "/set/11/0")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_pins(self):
        self.conn.request("GET", "/pins")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_getAll(self):
        self.conn.request("GET", "/get")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_getWrongPin(self):
        self.conn.request("GET", "/get/14")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 404)

    def test_getPin(self):
        self.conn.request("GET", "/get/11")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)

    def test_switchWrongPin(self):
        self.conn.request("GET", "/switch/14")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 404)

    def test_switch(self):
        self.conn.request("GET", "/switch/11")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)
        self.conn.request("GET", "/switch/11")
        res = self.conn.getresponse()
        self.assertEqual(res.status, 200)


if __name__ == '__main__':
    unittest.main()
