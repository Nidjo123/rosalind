
s = input()
t = input()

def hamming_distance(a, b):
    return len(list(filter(lambda x: x[0] != x[1], zip(a, b))))

print(hamming_distance(s, t))
