

def read_fasta(file_path):
    with open(file_path, 'r') as f:
        res = {}
        name = None
        dna = None
        for line in f.readlines():
            line = line.strip()
            if line.startswith('>'):
                if name is not None:
                    res[name] = dna
                name = line[1:]
                dna = ''
            else:
                dna += line.strip()
        if name is not None and name not in res:
            res[name] = dna
        return res
