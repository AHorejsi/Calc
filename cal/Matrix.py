class Matrix:
    def __init__(self, table):
        self.table = table

    def rowLength(self):
        return len(self.table)

    def columnLength(self):
        if self.rowLength() == 0:
            return 0
        else:
            return len(self.table[0])

    def __iter__(self):
        return self.table.__iter__()
