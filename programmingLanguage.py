

class ProgrammingLanguage():

    def __init__(self, typing, reflection, year, dynamic):

        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.dynamic = dynamic

    def is_dynamic(self):
        if self.typing == "Dynamic":
            self.dynamic = True


