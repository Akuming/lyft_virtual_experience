from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self, wear):
        self.wear = wear
    
    def needs_service(self):
        check = False
        sum = 0
        for i in range(len(self.wear)):
            sum = sum + self.wear[i]
        if sum >= 3:
            check = True
        return check


