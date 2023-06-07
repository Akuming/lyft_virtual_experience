import battery.battery_class

class NubbinBattery(battery.battery_class.BatteryClass):
    def __init__(self, current_date):
        self.current_date = current_date
    
    def needs_service(self):
        pass