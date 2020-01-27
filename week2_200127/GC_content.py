from __future__ import division

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
g_count = my_dna.count('G')
c_count = my_dna.count('C')

gc_content = (g_count + c_count) / length
print("GC content is " + str(gc_content))
