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


