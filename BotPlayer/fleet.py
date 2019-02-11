"""Module to declare fleets and the ships that make up the fleet"""
from ship import Ship

class Fleet(object):
    """Fleet is the container for all of the ships"""
    def __init__(self):
        self.b = Ship.ship_factory('battleship')
        self.d = Ship.ship_factory('destroyer')
        self.pb = Ship.ship_factory('patrolboat')
        self.s = Ship.ship_factory('submarine')
        self.ac = Ship.ship_factory('aircraftcarrier')

        self.f_damage = 0
        self.f_count = 5

    def sink_ship(self):
        self.f_damage += 1

    def fleet_sunk(self):
        if self.f_damage == self.f_count:
            return True 
        else:
            return False
