from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):

    def needs_service(self):
        service_threshold_date = self.engine.last_service_date.replace(year=self.engine.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced():
            return True
        else:
            return False
