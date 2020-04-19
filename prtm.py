import defs


P = input()

weight = sum([defs.monoisotopic_mass_table[c] for c in P])
print(weight)
