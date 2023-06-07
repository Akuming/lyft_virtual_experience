from abc import ABC, abstractclassmethod

class EngineClass(ABC):

    @abstractclassmethod
    def engine_should_be_serviced(self):
        pass