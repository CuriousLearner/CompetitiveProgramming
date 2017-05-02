def distance(dna_strand_1, dna_strand_2):
    hamming_distance = 0
    if len(dna_strand_1) != len(dna_strand_2):
    	raise ValueError("Both DNA strands must be of equal length")
    for k1, k2 in zip(dna_strand_1, dna_strand_2):
    	if k1 != k2:
    		hamming_distance += 1
    return hamming_distance
