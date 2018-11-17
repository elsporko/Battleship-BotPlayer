import unittest

from grid import M_grid, E_grid
from fleet import Fleet

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.m = M_grid()
        self.e = E_grid()

    def test_M_grid(self):
        """Create 'my' grid"""
        self.assertIsInstance(self.m, M_grid)

    def test_E_grid(self):
        """Create 'enemy' grid"""
        self.assertIsInstance(self.e, E_grid)

    def test_plot_piece(self):
        """Attempt to successfully plot all ships"""
        f = Fleet()
        b = f.b # Create battleship
        ac = f.ac # Create aircraft carrier
        d = f.d # Create destroyer
        pb = f.pb # Create patrol boat
        s = f.s # Create submarine

        """Test along 'x' axis"""
        self.assertTrue(self.m.plot_piece(b, ((1,1), (1,2), (1,3), (1,4), (1,5))))
        self.assertTrue(self.m.plot_piece(ac, ((2,1), (2,2), (2,3), (2,4), (2,5))))
        self.assertTrue(self.m.plot_piece(d, ((3,1), (3,2), (3,3), (3,4))))
        self.assertTrue(self.m.plot_piece(pb, ((4,1), (4,2))))
        self.assertTrue(self.m.plot_piece(s, ((5,1), (5,2), (5,3))))

    def test_plot_collision(self):
        """Validate plot_piece fails on collision"""
        f = Fleet()
        b = f.b # Create battleship
        ac = f.ac
        self.m.plot_piece(b, ((1,1), (1,2), (1,3), (1,4), (1,5)))
        self.assertFalse(self.m.plot_piece(ac, ((1,4), (1,5), (1,6), (1,7), (1,8))))

    def test_plot_out_of_bounds(self):
        f = Fleet()
        pb = f.pb
        self.assertFalse(self.m.plot_piece(pb, ((1,-1), (1,1))))
        self.assertFalse(self.m.plot_piece(pb, ((1,9), (1,10))))
        self.assertFalse(self.m.plot_piece(pb, ((-1,1), (1,1))))
        self.assertFalse(self.m.plot_piece(pb, ((9,1), (10,1))))

    def test_move_piece(self):
        f = Fleet()
        b = f.b # Create battleship
        """ Move piece back one space"""
        self.m.plot_piece(b, ((1,1), (1,2), (1,3), (1,4), (1,5)))
        self.assertTrue(self.m.move_piece(b.id, -1))

        """Move piece forward 3 spaces"""
        self.m.plot_piece(b, ((2,2), (2,3), (2,4), (2,5), (2,6)))
        self.assertTrue(self.m.move_piece(b.id, 3))

        """ Move piece back one space out of range"""
        self.m.plot_piece(b, ((0,1), (1,1), (1,2), (1,3), (1,4)))
        self.assertFalse(self.m.move_piece(b.id, -1))

        """Move piece forward 3 spaces out of range"""
        self.m.plot_piece(b, ((2,4), (2,5), (2,6), (2,7), (2,8)))
        self.assertFalse(self.m.move_piece(b.id, 3))
