from random import randrange
from Ship import Ship
from time import perf_counter


class Field:

    def __init__(self, size=6, ships=None):

        self.size = size

        self._field = self.gen_field()

        self.hidden_field = self.gen_field()

        if ships is None:

            self.needed_ships = {
                '3': 1,
                '2': 2,
                '1': 4
            }

        else:
            self.needed_ships = dict(ships)

        self.max_ship_size = max(list(map(int, self.needed_ships.keys())))

        self._health = 0

        for i in self.needed_ships.keys():
            self._health += int(i)*self.needed_ships[i]

    def gen_field(self):

        field = []

        for i in range(self.size+1):
            field.append([])

        field[0].append(' ')

        for i in range(1, self.size+1):

            field[0].append(str(i))
            field[i].append(str(i))

            for k in range(self.size):
                field[i].append('O')

        return field

    def generate_ships(self):

        while True:

            position = bool(randrange(2))

            if position:

                x1 = x2 = randrange(1, self.size+1)

                y1 = randrange(1, self.size+1)
                y2 = randrange(1, self.size+1)

            else:

                y1 = y2 = randrange(1, self.size+1)

                x1 = randrange(1, self.size+1)
                x2 = randrange(1, self.size+1)

            try:
                ship = Ship((x1, y1), (x2, y2), self.max_ship_size)

                if self.needed_ships.get(str(ship.size)) > 0:
                    self.add_ship(ship)
                    self.needed_ships[str(ship.size)] -= 1

            except ValueError:
                continue

            if sum(list(self.needed_ships.values())) == 0:
                break

    def add_ship(self, ship):

        if ship.first_coord == ship.second_coord:
            x, y = map(int, ship.first_coord)
            self.check_neighbors(x, y)
            self._field[x][y] = '■'

        else:

            need_to_fil = []

            if ship.first_coord[0] == ship.second_coord[0]:  # Horizontal

                x = ship.first_coord[0]

                y1 = min(ship.first_coord[1], ship.second_coord[1])
                y2 = max(ship.first_coord[1], ship.second_coord[1])

                for i in range(y1, y2+1):
                    self.check_neighbors(x, i)
                    need_to_fil.append([x, i])

            else:  # Vertical

                y = ship.first_coord[1]

                x1 = min(ship.first_coord[0], ship.second_coord[0])
                x2 = max(ship.first_coord[0], ship.second_coord[0])

                for i in range(x1, x2+1):
                    self.check_neighbors(i, y)
                    need_to_fil.append([i, y])

            for i in need_to_fil:
                self._field[i[0]][i[1]] = '■'

    def check_neighbors(self, x, y):

        size = self.size

        if self._field[x][y] == '■':
            raise ValueError('Slot already taken')

        elif x == size and y == size:
            if (
                self._field[size-1][size] == '■' or
                self._field[size][size-1] == '■'
            ):
                raise ValueError('Slot already taken')

        elif x == size:
            if (
                self._field[x][y-1] == '■' or
                self._field[x][y+1] == '■' or
                self._field[x-1][y] == '■'
            ):
                raise ValueError('Slot already taken')

        elif y == size:
            if (
                self._field[x-1][y] == '■' or
                self._field[x+1][y] == '■' or
                self._field[x][y-1] == '■'
            ):
                raise ValueError('Slot already taken')

        else:
            if (
                self._field[x][y-1] == '■' or
                self._field[x][y+1] == '■' or
                self._field[x-1][y] == '■' or
                self._field[x+1][y] == '■'
            ):
                raise ValueError('Slot already taken')

    def attacked(self, x, y):

        if self._field[x][y] == '■':
            print('Hit!')
            print('-------------------------')
            self._field[x][y] = 'X'
            self.hidden_field[x][y] = 'X'
            self._health -= 1
            return False

        elif self._field[x][y] == 'O':
            print('Miss!')
            print('-------------------------')
            self._field[x][y] = 'T'
            self.hidden_field[x][y] = 'T'
            return True

        else:
            raise ValueError('You cant attack in the same place')

    @property
    def field(self):
        return self._field

    @property
    def health(self):
        return self._health
