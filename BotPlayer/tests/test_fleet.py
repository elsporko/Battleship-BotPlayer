import unittest
import random

from fleet import Fleet

class TestFleet(unittest.TestCase):

    def setUp(self):
        self.f = Fleet()

    def test_fleetcreate(self):
        """Ships are accessible from Fleet module"""
        self.assertEqual(self.f.ac.label, 'AircraftCarrier')
        self.assertEqual(self.f.d.label, 'Destroyer')
        self.assertEqual(self.f.s.label, 'Submarine')
        self.assertEqual(self.f.b.label, 'Battleship')
        self.assertEqual(self.f.pb.label, 'PatrolBoat')

    def test_fleetdamage(self):
        """Damage done to portion of a ship via Fleet module"""
        h = lambda s : 2 ** random.randint(0, s + 1)

        d = h(self.f.b.size)
        self.f.b.do_damage(d)
        self.assertEqual(self.f.b.damage, d)

        d = h(self.f.d.size)
        self.f.d.do_damage(d)
        self.assertEqual(self.f.d.damage, d)

        d = h(self.f.pb.size)
        self.f.pb.do_damage(d)
        self.assertEqual(self.f.pb.damage, d)

        d = h(self.f.s.size)
        self.f.s.do_damage(d)
        self.assertEqual(self.f.s.damage, d)

        d = h(self.f.ac.size)
        self.f.ac.do_damage(d)
        self.assertEqual(self.f.ac.damage, d)

    def test_sunk(self):
        """Test ship sunk from Fleet module"""
        # Loop through a ship size and hit it until
        # it has sunk. Test after each hit and check for
        # appropriate status.

        # Create a tuple of all ships so they can be iterated through
        # for sunk tests
        fleet = (self.f.ac, self.f.d, self.f.s, self.f.b, self.f.pb)

        for f in fleet:
            for i in range(0, f.size -1):
                f.do_damage(2**i)
                self.assertFalse(f.is_sunk())
        
            f.do_damage(2**(f.size -1))
            self.assertTrue(f.is_sunk())

            if f.is_sunk():
                self.f.sink_ship(f)

        self.assertTrue(self.f.fleet_sunk())
