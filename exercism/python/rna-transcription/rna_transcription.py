def to_rna(dna_strand):
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    try:
        rna_strand = ''.join([mapping[x] for x in dna_strand])
    except KeyError:
        rna_strand = ''
    return rna_strand
