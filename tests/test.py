from http.client import HTTPConnection
import unittest
import socket

class TestClient(unittest.TestCase):
    def test_index(self):
        status = HTTPConnection("localhost", 5000)