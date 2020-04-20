
with open(input(), 'r') as f:
    s, t = map(lambda s: s.strip(), f.readlines())
    last_pos = 0
    while (pos := s.find(t, last_pos)) >= 0:
        last_pos = pos + 1
        print(last_pos, end=' ')
    print()
