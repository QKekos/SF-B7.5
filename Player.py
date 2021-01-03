from Field import Field
from Ship import Ship


class Player(Field):
    def input_ship(self):

        try:
            ship = self.coord_input_try('Input start/end ship coordinates\n')

            if self.needed_ships[str(ship.size)] > 0:
                self.add_ship(ship)
                self.needed_ships[str(ship.size)] -= 1

        except ValueError:
            pass

        if sum(list(self.needed_ships.values())) == 0:
            return False

        return True

    def coord_input_try(self, text):

        try:
            input_string = input(text)
            print('-------------------------')

            if input_string.count(' ') == 1:
                x, y = map(int, input_string.split())
                ship = Ship((x, y), self.max_ship_size)

            else:
                x1, y1, x2, y2 = map(int, input_string.split())
                ship = Ship((x1, y1), (x2, y2), self.max_ship_size)

            return ship

        except ValueError:
            return self.coord_input_try('Input correct values:\n')
