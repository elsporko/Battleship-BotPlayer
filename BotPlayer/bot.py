import grid
import fleet

f = Fleet()
g = Grid()

# Make my own fleet
b  =         self.b = Ship.ship_factory('battleship')
d  =         self.d = Ship.ship_factory('destroyer')
pb =         self.pb = Ship.ship_factory('patrolboat')
s  =         self.s = Ship.ship_factory('submarine')
ac =         self.ac = Ship.ship_factory('aircraftcarrier')

my_fleet = (b, d, pb, s, ac)

for f in my_fleet:
    f.initial_
