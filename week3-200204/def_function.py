def get_gc_content(dna):
    length = len(dna)
    dna = dna.upper()
    g_count = dna.count('G')
    c_count = dna.count('C')
    gc_content = float(g_count + c_count)/float(length)
    return gc_content
