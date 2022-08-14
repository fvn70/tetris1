class Field:
    items = []

    def __init__(self, cols, rows):
        self.n = rows
        self.m = cols

    def add_item(self, p):
        self.items = []
        self.items.append(p)

    def down(self, p):
        p.down(self.m)

    def left(self, p):
        p.left(self.m)

    def right(self, p):
        p.right(self.m)

    def rotate(self, p):
        p.rotate()

    def draw(self):
        lst = []
        for p in self.items:
            lst += p.shapes[p.idx]
        k = 0
        print()
        for r in range(self.n):
            s = ''
            for c in range(self.m):
                s += '0 ' if k in lst else '- '
                k += 1
            print(s.strip())

class Figure:

    def __init__(self, name, shapes):
        self.name = name
        self.shapes = shapes
        self.idx = 0
        self.turn = 0
        self.turns = len(shapes)

    def down(self, m):
        self.shapes = [[p[j] + m for j in range(4)] for p in self.shapes]

    def left(self, m):
        self.shapes = [[p[j] - 1 if p[j] % m > 0 else p[j] + m - 1 for j in range(4)] for p in self.shapes]

    def right(self, m):
        self.shapes = [[p[j] + 1 if p[j] % m < m - 1 else p[j] - m + 1 for j in range(4)] for p in self.shapes]

    def rotate(self):
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


fig = input()
m, n = input().split()
# m, n = '10', '20'
g = Field(int(m), int(n))
g.draw()
f = Figure(fig, dic[fig].copy())
g.add_item(f)
g.draw()

while True:
    cmd = input()
    if cmd == 'exit':
        break
    elif cmd == 'down':
        pass
    elif cmd == 'left':
        g.left(f)
    elif cmd == 'right':
        g.right(f)
    elif cmd == 'rotate':
        g.rotate(f)

    g.down(f)
    g.draw()
