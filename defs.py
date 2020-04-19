

RNA_codons = {}

with open('rna_codons.txt') as f:
    for line in f:
        parts = line.split()
        for i in range(0, len(parts), 2):
            RNA_codons[parts[i]] = parts[i + 1]

assert len(RNA_codons) == 2**6
for k, v in RNA_codons.items():
    assert len(k) == 3

monoisotopic_mass_table = {}

with open('monoisotopic_mass_table.txt') as f:
    for line in f:
        protein, mass = line.split()
        monoisotopic_mass_table[protein] = float(mass)
