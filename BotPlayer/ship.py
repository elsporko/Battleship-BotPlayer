"""A bottle to contain the ships"""
class Ship(object):
    """Class to define ships"""
    def __init__(self):
        pass

    def ship_factory(ship_type):
        """Build the ships"""
        if ship_type == 'aircraftcarrier':
            return AircraftCarrier()
        if ship_type == 'destroyer':
            return Destroyer()
        if ship_type == 'submarine':
            return Submarine()
        if ship_type == 'battleship':
            return Battleship()
        if ship_type == 'patrolboat':
            return PatrolBoat()

    ship_factory = staticmethod(ship_factory)

class AircraftCarrier(Ship):
    """Build an aircraft carrier"""
    def __init__(self):
        super().__init__()
        self.size = 5
        self.id = 'aircraftCarrier'
        self.label = 'AircraftCarrier'
        self.mask = 31

class Destroyer(Ship):
    """Build a destroyer"""
    def __init__(self):
        super().__init__()
        self.size = 4
        self.id = 'destroyer'
        self.label = 'Destroyer'
        self.mask = 31

class Submarine(Ship):
    """Build a submarine"""
    def __init__(self):
        super().__init__()
        self.size = 3
        self.id = 'submarine'
        self.label = 'Submarine'
        self.mask = 31

class Battleship(Ship):
    """Build a battleship"""
    def __init__(self):
        super().__init__()
        self.size = 5
        self.id = 'battleship'
        self.label = 'Battleship'
        self.mask = 31

class PatrolBoat(Ship):
    """Build a patrol boat"""
    def __init__(self):
        super().__init__()
        self.size = 2
        self.id = 'patrolboat'
        self.label = 'PatrolBoat'
        self.mask = 31

