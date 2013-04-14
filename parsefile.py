class Parser():
    def __init__(self, string, endof):
        self.string = string
        self.endof = endof
        self.list = []

    def run(self):
        self.parse()
        self.clean()

        return self.list

    def parse(self):
        self.list = str(self.string).split(str(self.endof))
        if self.list[len(self.list) -1 ] == "\n":
            del(self.list[len(self.list) - 1])

    def clean(self):
        for item in self.list:
            item.replace(self.endof,"")

class Joiner():
    pass

class Opener():
    def __init__(self, fileName):
        import os
        self.fileName = os.path.join(os.path.realpath(os.path.dirname(__file__)), fileName)

    def open(self):
        with open(self.fileName,"r") as fileC:
            return fileC.read()


