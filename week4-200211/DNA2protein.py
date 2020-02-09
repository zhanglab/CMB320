import sys

# Set DNA string, DNA string direction, and if it is template string
dna_raw = 'AATTTGCTTGGCAAA'
dna = dna_raw.upper()
dna_dir = True
temp = False


# Step 1: Define a function that can convert single DNA string to RNA string
def transcription(dna, dir, temp):
    rna = ''
    dna_map_rna = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    if dir:             # 'if dir' is the same as 'if dir == True'
        if temp:        # 'if temp' is the same as 'if temp == True'
            for n in dna[::-1]:
                rna += dna_map_rna[n]
        else:
            rna = dna.replace('T', 'U')
    else:
        if temp:
            for n in dna:
                rna += dna_map_rna[n]
        else:
            rna = dna[::-1].replace('T', 'U')
    return rna


# Using transcription() function to get the RNA string
rna_string = transcription(dna, dna_dir, temp)

# RNA codon table
rna_codon = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
             }


# Step 2: Define a function to translate RNA string to protein sequence
def translation(rna):
    protein_string = ""
    for i in range(0, len(rna) - len(rna) % 3, 3):
        if rna_codon[rna[i:i + 3]] == "STOP":
            break
        protein_string += rna_codon[rna[i:i + 3]]
    return protein_string


# Using transcription() function to get the RNA string
protein = translation(rna_string)

# Print the protein string
print("Protein String: ", protein)
