import reader


def gc_content(s):
    gc_count = s.count('G') + s.count('C')
    return gc_count / len(s)

data = reader.read_fasta(input())

max_gc = 0
max_id = None
for dna_id, dna in data.items():
    gc_percentage = gc_content(dna)
    if gc_percentage > max_gc:
        max_gc = gc_percentage
        max_id = dna_id
print(max_id)
print(max_gc * 100)
        
