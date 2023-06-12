import unittest
from tires.octoprime import Octoprime

class OctoPrimeTest(unittest.TestCase):
    def tires_should_be_serviced(self):
        wear = [0.8, 0.8, 0.8, 0.8]
        tires = Octoprime(wear)
        self.assertTrue(tires.needs_service())
    
    def tires_should_not_be_serviced(self):
        wear = [0.5, 0.5, 0.5, 0.5]
        tires = Octoprime(wear)
        self.assertFalse(tires.needs_service())