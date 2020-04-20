import collections

import reader

dnas = reader.read_fasta(input())

DNA = 'ACGT'


dna_len = len(list(dnas.values())[0])
counts = []
for i in range(dna_len):
    s = ''.join([x[i] for x in dnas.values()])
    counts.append(collections.Counter(s))

consensus = ''.join(c.most_common()[0][0] for c in counts)

print(consensus)
for letter in DNA:
    print(letter + ': ', end='')
    print(' '.join(str(c[letter]) for c in counts))
    
