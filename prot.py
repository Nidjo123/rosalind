import itertools

import defs


def _iter_by_n(a, n):
    for i in range(0, len(a), n):
        yield a[i:i+n]


file_path = input()
with open(file_path, 'r') as f:
    s = f.read().strip()
    translated = [defs.RNA_codons[x] for x in _iter_by_n(s, 3)]
    res = ''.join(itertools.takewhile(lambda x: x != 'Stop', translated))
    print(res)
    
