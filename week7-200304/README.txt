##### This folder contains files related to making phylogenetic tree, using ermB protein ID to organism name and annotation. The detailed tutorial is in TopHat: "Phylogenetic tree-Tutorial" #####

# 1. seqdump.txt: 10 protein sequences downloaded from NCBI blast results.

# 2. clustalw.phy : Alignment of the 10 protein sequences, suing Clustawl

# 3. file.nwk: file of phylogenetic tree in Newick format

# 4. ermB_map.tsv: A TSV file to map protein ID to gene annotation and organism name

# 5. file.tre: a tree file to upload in Dengroscope in order to get midpoin. I get this file through command:
cp file.nwk file.tre

# 6. change_iTOL_label.txt: used to change leaf labels in iTOL

### ermB: This protein produces a dimethylation of the adenine residue at position 2085 in 23S rRNA, resulting in reduced affinity between ribosomes and macrolide-lincosamide-streptogramin B antibiotics. (Based on uniport: https://www.uniprot.org/uniprot/P0A4D5)