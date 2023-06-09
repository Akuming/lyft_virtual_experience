import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
#from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced)

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
