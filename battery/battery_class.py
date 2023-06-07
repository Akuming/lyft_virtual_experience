from abc import ABC, abstractclassmethod

class BatteryClass(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def needs_service(self):
        pass