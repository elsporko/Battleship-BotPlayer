import unittest
import sys
import random

from ship import Ship

class TestShips(unittest.TestCase):

    def setUp(self):
        self.b = Ship.ship_factory('battleship')
        self.d = Ship.ship_factory('destroyer')
        self.pb = Ship.ship_factory('patrolboat')
        self.s = Ship.ship_factory('submarine')
        self.ac = Ship.ship_factory('aircraftcarrier')


    def test_battleship(self):
        """Create Battleship"""
        self.assertEqual(self.b.size, 5)
        self.assertEqual(self.b.id, 'battleship')
        self.assertEqual(self.b.label, 'Battleship')

    def test_aircraftcarrier(self):
        """Create Aircraft Carrier"""
        self.assertEqual(self.ac.size, 5)
        self.assertEqual(self.ac.id, 'aircraftCarrier')
        self.assertEqual(self.ac.label, 'AircraftCarrier')

    def test_destroyer(self):
        """Create Destroyer"""
        self.assertEqual(self.d.size, 4)
        self.assertEqual(self.d.id, 'destroyer')
        self.assertEqual(self.d.label, 'Destroyer')

    def test_submarine(self):
        """Create Submarine"""
        self.assertEqual(self.s.size, 3)
        self.assertEqual(self.s.id, 'submarine')
        self.assertEqual(self.s.label, 'Submarine')

    def test_patrolboat(self):
        """Create Patrol Boat"""
        self.assertEqual(self.pb.size, 2)
        self.assertEqual(self.pb.id, 'patrolboat')
        self.assertEqual(self.pb.label, 'PatrolBoat')

    def test_damage(self):
        """Damage done to portion of a ship"""
        h = lambda s : 2 ** random.randint(0, s + 1)

        d = h(self.b.size)
        self.b.do_damage(d)
        self.assertEqual(self.b.damage, d)

        d = h(self.d.size)
        self.d.do_damage(d)
        self.assertEqual(self.d.damage, d)

        d = h(self.pb.size)
        self.pb.do_damage(d)
        self.assertEqual(self.pb.damage, d)

        d = h(self.s.size)
        self.s.do_damage(d)
        self.assertEqual(self.s.damage, d)

        d = h(self.ac.size)
        self.ac.do_damage(d)
        self.assertEqual(self.ac.damage, d)

    def test_sunk(self):
        """Test ship sunk"""
        # Loop through a ship size and hit it until
        # it has sunk. Test after each hit and check for
        # appropriate status.
        for i in range(0, self.b.size -1):
            self.b.do_damage(2**i)
            self.assertFalse(self.b.is_sunk())
    
        self.b.do_damage(2**(self.b.size -1))
        self.assertTrue(self.b.is_sunk())
