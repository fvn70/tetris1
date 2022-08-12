O = [[5, 6, 9, 10]]
I = [[1, 5, 9, 13], [4, 5, 6, 7]]
S = [[6, 5, 9, 8], [5, 9, 10, 14]]
Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

dic = {'O': O, 'I': I, 'S': S, 'Z': Z, 'L': L, 'J': J, 'T': T, }

def draw(letter):
    pieces = dic[letter]
    r = len(pieces)
    pieces = (4 // r + 1) * pieces
    p = []
    for i in range(6):
        for r in range(4):
            for c in range(4):
                k = r * 4 + c
                print('0 ' if k in p else '- ', end='')
            print()
        print()
        if i < 5:
            p = pieces[i]


draw(input())
