#from engine.model.calliope import Calliope
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime
from car import Car

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tires = Octoprime(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tires = Octoprime(tire_wear)
        car = Car(engine, battery, tires)
        return car