from tires.tires import Tires

class Carrigan(Tires):
    def __init__(self, wear):
        self.wear = wear
    
    def needs_service(self):
        check = False
        for i in range(len(self.wear)):
            if self.wear[i] >= 0.9:
                check = True
        return check
            