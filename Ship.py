class Ship:

    def __init__(self, first_coord, second_coord=None, max_ship_size=3):

        second_coord = first_coord if second_coord is None else second_coord

        if first_coord == second_coord:
            self.size = 1

        else:
            self.max_ship_size = max_ship_size
            self.size = self.check_coords(first_coord, second_coord)

        self.first_coord = first_coord
        self.second_coord = second_coord

    def check_coords(self, first_coord, second_coord):

        x1 = first_coord[0]
        y1 = first_coord[1]

        x2 = second_coord[0]
        y2 = second_coord[1]

        if (
                (x1 != x2 and y1 - y2 != 0) or  # Проверка лежит ли корабль на 1 вертикальной линии
                (y1 != y2 and x1 - x2 != 0) or  # Проверка лежит ли корабль на 1 горизонтальной линии
                (abs(x1 - x2) >= self.max_ship_size or abs(y1 - y2) >= self.max_ship_size)  # Проверка длины корабля
        ):
            raise ValueError(f"Ship can't be bigger than 1x{self.max_ship_size}")

        return abs(x1 - x2) + 1 if y1 == y2 else abs(y1 - y2) + 1
