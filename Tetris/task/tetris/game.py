import numpy as np

class Field:
    items = []
    saved = []

    def __init__(self, cols, rows):
        self.n = rows
        self.m = cols

    def add_item(self, p):
        self.items = []
        self.items.append(p)

    def down(self, p):
        return p.down(self, self.m, self.n)

    def left(self, p):
        p.left(self.m)

    def right(self, p):
        p.right(self.m)

    def rotate(self, p):
        p.rotate()

    def draw(self):
        lst = []
        for p in self.items:
            if p.live:
                lst += p.shapes[p.idx]
        lst += self.saved
        k = 0
        print()
        for r in range(self.n):
            s = ''
            for c in range(self.m):
                s += '0 ' if k in lst else '- '
                k += 1
            print(s.strip())

    def down_all(self):
        v_max = self.m * (self.n - 1)
        while np.intersect1d(self.saved, range(v_max, v_max + self.m)).size == self.m:
            self.saved = [v + self.m for v in self.saved if v < v_max]

class Figure:

    def __init__(self, name, shapes):
        self.name = name
        self.shapes = shapes
        self.live = True
        self.idx = 0
        self.turn = 0
        self.turns = len(shapes)

    def down(self, g, m, n):
        row = n
        if self.live:
            p = self.shapes[self.idx]
            p1 = [v + m for v in p]
            v0 = max([v // m for v in p])
            if np.intersect1d(g.saved, p1).size == 0:
                if v0 < n - 1:
                    self.shapes = [[p[j] + m for j in range(4)] for p in self.shapes]
                if v0 == n - 2:
                    self.live = False
                    g.saved += p1
            else:
                self.live = False
                g.saved += p
            if len(g.saved) > 0:
                row = min(g.saved) // m
        return row

    def left(self, m):
        if self.live and min([v % m for v in self.shapes[self.idx]]) > 0:
            self.shapes = [[p[j] - 1 for j in range(4)] for p in self.shapes]

    def right(self, m):
        if self.live and max([v % m for v in self.shapes[self.idx]]) < m - 1:
            self.shapes = [[p[j] + 1 for j in range(4)] for p in self.shapes]

    def rotate(self):
        if self.live:
            self.turn += 1
            self.idx = self.turn % self.turns


O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

dic = {'O': O, 'I': I, 'S': S, 'Z': Z, 'L': L, 'J': J, 'T': T, }

m, n = input().split()
# m, n = '10', '20'
g = Field(int(m), int(n))
g.draw()

while True:
    cmd = input()
    if cmd == 'exit':
        break
    elif cmd == 'piece':
        cmd = input()
        f = Figure(cmd, dic[cmd].copy())
        g.add_item(f)
        g.draw()
        continue
    elif cmd == 'down':
        pass
    elif cmd == 'break':
        g.down_all()
    elif cmd == 'left':
        g.left(f)
    elif cmd == 'right':
        g.right(f)
    elif cmd == 'rotate':
        g.rotate(f)

    row = g.down(f)
    g.draw()
    if row < 1:
        print('\nGame Over!')
        break
