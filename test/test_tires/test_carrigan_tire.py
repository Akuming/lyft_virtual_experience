import unittest
from tires.carrigan import Carrigan

class CarriganTest(unittest.TestCase):
    def tires_should_be_serviced(self):
        wear = [0.95, 0.8, 0.8, 0.8]
        tires = Carrigan(wear)
        self.assertTrue(tires.needs_service())
    
    def tires_should_not_be_serviced(self):
        wear = [0.8, 0.8, 0.8, 0.8]
        tires = Carrigan(wear)
        self.assertFalse(tires.needs_service())