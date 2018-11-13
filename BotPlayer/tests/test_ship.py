import unittest
import sys
print ("path ", sys.path)

from ship import Ship

class TestShips(unittest.TestCase):

    def setUp(self):
        self.b = Ship.ship_factory('battleship')
        self.d = Ship.ship_factory('destroyer')
        self.pb = Ship.ship_factory('patrolboat')
        self.s = Ship.ship_factory('submarine')
        self.ac = Ship.ship_factory('aircraftcarrier')


    def test_battleship(self):
        self.assertEqual(self.b.size, 5)
        self.assertEqual(self.b.id, 'battleship')
        self.assertEqual(self.b.label, 'Battleship')
        self.assertEqual(self.b.mask, 31)

    def test_aircraftcarrier(self):
        self.assertEqual(self.ac.size, 5)
        self.assertEqual(self.ac.id, 'aircraftCarrier')
        self.assertEqual(self.ac.label, 'AircraftCarrier')
        self.assertEqual(self.ac.mask, 31)

    def test_destroyer(self):
        self.assertEqual(self.d.size, 4)
        self.assertEqual(self.d.id, 'destroyer')
        self.assertEqual(self.d.label, 'Destroyer')
        self.assertEqual(self.d.mask, 31)

    def test_submarine(self):
        self.assertEqual(self.s.size, 3)
        self.assertEqual(self.s.id, 'submarine')
        self.assertEqual(self.s.label, 'Submarine')
        self.assertEqual(self.s.mask, 31)

    def test_patrolboat(self):
        self.assertEqual(self.pb.size, 2)
        self.assertEqual(self.pb.id, 'patrolboat')
        self.assertEqual(self.pb.label, 'PatrolBoat')
        self.assertEqual(self.pb.mask, 31)

if __name__ == '__main__':
    unittest.main()
