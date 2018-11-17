"""Grid creation and management. Includes base grid class and classes
   for own grid and enemy grids"""
class Grid(object):
    def __init__(self):
        # Map of ship locations
        self.chart =[[0 for x in range(10)] for y in range(10)]

class M_grid(Grid):
    """Means and methods to control own board"""
    def __init__(self):
        super().__init__()
        self.ship_map = {}

    def __detect_collision (self, ship_id, x, y):
        if self.chart[x][y] != 0 and self.chart[x][y] != ship_id:
            return True
        return False

    def __detect_over_boundary (self, x, y):
        if x < 0 or y < 0 or x >= len(self.chart) or y >= len(self.chart[x]):
            return True
        return False

    def __detect_orientation (self, plot1, plot2):
        if plot1[0] == plot2[0]:
            return 'x'
        return 'y'

    def __validate_piece (self, ship_id, x, y):
         # TODO Will become validation method
         if self.__detect_over_boundary(x, y):
             return False

         if self.__detect_collision(ship_id, x, y):
             return False

         return True

    def plot_piece (self, ship_type, coords):
        tmp_chart = self.chart
        orientation = self.__detect_orientation(coords[0], coords[1])

        for c in coords:
            x,y = c

            if not self.__validate_piece(ship_type.id, x, y):
                return False

            tmp_chart[x][y] = ship_type.id

        self_chart = tmp_chart
        self.ship_map[ship_type.id] = {"size": ship_type.size, "orientation": orientation, "start_coord": coords[0]}
        return True

    #def build_ship(self, current_location, spaces):
    #    orientation = current_location.orientation
    #    x,y = current_location.start_coord

    #    if orientation == 'x':
    #        x = x + spaces
    #    if orientation == 'y':
    #        y = y + spaces

    #    for i in range(current_location.size):

    def move_piece(self, ship_id, spaces):
        # move piece takes the ship and the number of spaces to move it where
        # moving to the left or up will be represented by a negative number 
        # and right or down will be a positive number
        tmp_chart = self.chart
        orientation = self.ship_map[ship_id]['orientation']
        x,y = self.ship_map[ship_id]['start_coord']

        start_coord = ()
        if spaces < 0:
            if orientation == 'x':
                y = y + spaces
            if orientation == 'y':
                x = x + spaces
            start_coord = (x,y)
        elif spaces > 0:
            if orientation == 'x':
                y = self.ship_map[ship_id]['start_coord'][1] + self.ship_map[ship_id]['size'] - 1
            if orientation == 'y':
                x = self.ship_map[ship_id]['start_coord'][0] + self.ship_map[ship_id]['size'] - 1
       
        # Work on adding the 'new' spaces first so we can bail if validation fails
        for i in range (abs(spaces) + 1):
            if not self.__validate_piece(ship_id, x, y):
                return False

            tmp_chart[x][y] = ship_id
            if orientation == 'x':
                y = y + 1
            if orientation == 'y':
                x = x + 1

        # Now go remove the old spaces
        if spaces < 0:
            if orientation == 'x':
                y = self.ship_map[ship_id]['start_coord'][1] + self.ship_map[ship_id]['size'] + spaces
            if orientation == 'y':
                x = self.ship_map[ship_id]['start_coord'][0] + self.ship_map[ship_id]['size'] + spaces
        elif spaces > 0:
            start_coord = (x,y)
            x,y = self.ship_map[ship_id]['start_coord']

        for i in range (abs(spaces) + 1):
            if x > len(tmp_chart) or y > len(tmp_chart[x]):
                break
            tmp_chart[x][y] = 0
            if orientation == 'x':
                y = y + 1
            if orientation == 'y':
                x = x + 1

        self_chart = tmp_chart
        self.ship_map[ship_id]['start_coord'] = start_coord
        return True

    def pivot_piece(self):
        pass

class E_grid(Grid):
    """Means and methods to monitor opponent board(s)"""
    def __init__(self):
        super().__init__()
