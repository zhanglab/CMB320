# Step 1: Define a function that can convert single DNA string to RNA string
def transcription(dna, dir, temp):
    rna = ''
    dna_map_rna = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    if dir:             # 'if dir' is the same as 'if dir == True'
        if temp:        # 'if temp' is the same as 'if temp == True'
            for n in dna[::-1]:
                rna += dna_map_rna[n]
    return(rna)

dna = 'AGCAT'
rna = transcription(dna, True, True)
print(rna)
