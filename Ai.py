from Field import Field


class Ai(Field):

    @property
    def field(self):
        return self.hidden_field
