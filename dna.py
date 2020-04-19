import collections

data = input()
dna_count = collections.Counter(data)

for c in 'ACGT':
    print(dna_count[c], end=' ')
print()


