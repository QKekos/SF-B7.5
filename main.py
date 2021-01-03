from Ai import Ai
from Player import Player
from random import randrange


class Game:

    def __init__(self, player_, auto_player):

        self.queue = True

        self.player = player_
        self.ai = auto_player

        self.printed_ = False

    def manual_turn(self, text='Input attack coordinates:\n'):

        try:
            input_string = input(text)
            print('-------------------------')
            x, y = map(int, input_string.split())

            if self.ai.attacked(x, y):
                self.queue = not self.queue

        except ValueError:
            return self.manual_turn('Input correct values:\n')

    def auto_turn(self):

        x, y = randrange(1, 7), randrange(1, 7)
        try:
            if self.player.attacked(x, y):
                self.queue = not self.queue

        except ValueError:
            return self.auto_turn()

    def play(self):

        while player.health > 0 and ai.health > 0:

            if self.queue:
                
                self.manual_turn()

            else:
                self.auto_turn()

            print_fields()

        print('Ai wins!' if player.health == 0 else 'You win!')
        print('-------------------------')


def print_fields():
    global_field = []

    for i in range(len(player.field)):
        global_field.append(player.field[i] + [' ' * 10] + ai.field[i])

    for i in range(len(global_field) - 1):

        for k in global_field[i]:
            print('| ' + k, end=' ')

        print('|\n')

    for i in global_field[-1]:
        print('| ' + i, end=' ')

    print('|')

    print('-------------------------')


def place_mode_input_try(text):
    input_string = input(text)
    print('-------------------------')

    if input_string == 'manual' or input_string == 'auto':
        return input_string

    return place_mode_input_try('Input correct value:\n')


def field_size_input_try(text):
    try:
        print('-------------------------')
        size_ = int(input(text))
        print('-------------------------')

        if 6 <= size_ <= 12:
            return size_

        else:
            return field_size_input_try('Input correct value:\n')

    except ValueError:
        return field_size_input_try('Input correct value:\n')


def ships_count_input_try(text=None):

    global ships

    for i in range(1, 5):

        if ships[str(i)] == 0:

            try:
                if text is None:
                    text = f'Input {i}-slot ship count [0, 4]:\n'

                ship_count = input(text)
                print('-------------------------')
                ship_count = int(ship_count)

                if 0 <= ship_count <= 4:

                    ships[str(i)] = ship_count
                    break

                else:
                    return ships_count_input_try('Input correct value:\n')

            except ValueError:
                return ships_count_input_try('Input correct value:\n')

    if ships.get(str(i+1)) == 0:
        return ships_count_input_try()


if __name__ == '__main__':

    size = field_size_input_try('Input field size [6, 12]:\n')

    ships = {
        '4': 0,
        '3': 0,
        '2': 0,
        '1': 0
    }

    ships_count_input_try()

    player = Player(size, ships)
    ai = Ai(size, ships)

    print_fields()

    if place_mode_input_try('Input placing ships mode: manual/auto:\n') == 'auto':
        player.generate_ships()

    else:
        while player.input_ship():
            print_fields()

    ai.generate_ships()

    print_fields()

    game = Game(player, ai)
    game.play()
