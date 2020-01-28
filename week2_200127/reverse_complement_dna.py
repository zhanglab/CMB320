raw_my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
my_dna = raw_my_dna.upper()
replacement1 = my_dna.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')
reverse_comple_dna = replacement4[::-1]

print('          Original DNA: {}'.format(raw_my_dna))
print('Reverse Complement DNA: {}'.format(reverse_comple_dna.upper()))
