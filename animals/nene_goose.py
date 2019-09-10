from animals import Animal
# from interfaces import IFlying
from interfaces import Identifiable

class Nene_Goose(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Bird")
        # IFlying.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Grass", "Weedy Plants", "Berries"]