class Maze:
    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.compos = []

    def __init__(self, size):
        self.size = size
        self.cells = [[self.Cell(i, j) for j in range(size)] for i in range(size)]

    def __setitem__(self, key, val):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]

        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)):
                if val == '·':
                    if self.cells[x1][j+1] not in self.cells[x1][j].compos:
                        self.cells[x1][j].compos.append(self.cells[x1][j+1])
                        self.cells[x1][j+1].compos.append(self.cells[x1][j])
                elif val == '█':
                    if self.cells[x1][j+1] in self.cells[x1][j].compos:
                        self.cells[x1][j].compos.remove(self.cells[x1][j+1])
                        self.cells[x1][j+1].compos.remove(self.cells[x1][j])
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)):
                if val == '·':
                    if self.cells[i+1][y1] not in self.cells[i][y1].compos:
                        self.cells[i][y1].compos.append(self.cells[i+1][y1])
                        self.cells[i+1][y1].compos.append(self.cells[i][y1])
                elif val == '█':
                    if self.cells[i+1][y1] in self.cells[i][y1].compos:
                        self.cells[i][y1].compos.remove(self.cells[i+1][y1])
                        self.cells[i+1][y1].compos.remove(self.cells[i][y1])

    def __getitem__(self, key):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]

        routes = set()
        cur = set(self.cells[x1][y1].compos)
        prev = set()

        while cur - prev:
            prev |= cur
            tmp = set(cur)
            for i in tmp:
                if i not in routes:
                    routes.add(i)
                    cur |= set(i.compos)
            if self.cells[x2][y2] in cur:
                return True
        return False

    def __str__(self):
        cell = [['█'] * (2*self.size+1) for _ in range(2*self.size+1)]
        for i in range(self.size):
            for j in range(self.size):
                cell[1 + 2*j][1 + 2*i] = '·'
                for n in self.cells[i][j].compos:
                    dx = n.x - self.cells[i][j].x
                    dy = n.y - self.cells[i][j].y
                    cell[1 + 2*j + dy][1 + 2*i + dx] = '·'
        return '\n'.join(map(''.join, cell))




import sys
exec(sys.stdin.read())

