
data = input()

pairs = {'A': 'T', 'C': 'G'}
pairs.update({v: k for k, v in pairs.items()})

other_strand = ''.join(reversed([pairs[c] for c in data]))
print(other_strand)
