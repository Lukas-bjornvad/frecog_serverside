import unittest
from connection.connector import DB_connection
from settings.pathing import os_parse_path


class Tests(unittest.TestCase):
    def test_connection(self):
       self.assertIsNotNone(DB_connection())
    
    #def test_pathing(self):
    #    img = "dope"
    #    self.assertIsNotNone(os_parse_path(img))
