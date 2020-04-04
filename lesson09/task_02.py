"""2. Закодируйте любую строку по алгоритму Хаффмана."""

from collections import Counter, deque


class Node:
    def __init__(self, value, wight, left=None, right=None):
        self.value = value
        self.wight = wight
        self.left = left
        self.right = right


def generate_codes(tree, code={}, path=''):
    if tree and tree.value and tree.value not in code:
        code[tree.value] = path
    if tree and not tree.value:
        generate_codes(tree.left, code, path=f'{path}0')
        generate_codes(tree.right, code, path=f'{path}1')
    return code


def huffman(s):
    h = deque([Node(v, w) for v, w in sorted(Counter(s).items())])
    while True:
        a = h.popleft()
        b = h.popleft()
        weight = a.wight + b.wight
        if not h:
            h.append(Node(None, weight, left=a, right=b))
            break
        for i in range(len(h)):
            if h[len(h) - 1].wight <= weight:
                h.append(Node(None, weight, left=a, right=b))
                break
            elif h[i].wight > weight:
                h.insert(i, Node(None, weight, left=a, right=b))
                break
    return h[0]


s = 'beep boop beer!'  # для проверки
s2 = 'на дворе дрова.'

def main(s):
    bin_s = ' '.join([bin(ord(ss)) for ss in s])
    h = huffman(s)
    code = generate_codes(h, code={})
    print(f'\nСтрока: {s}\nВ двоичном виде: \n{bin_s}')
    print('Коды Хофмана: ', *code.items(), sep='\n')
    print('Код с пробелами, для удобства: \n', ' '.join([code[k] for k in s]))
    return ''.join([code[k] for k in s])

print(main(s))
print(main(s2))
