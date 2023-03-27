# Ask user for protein sequence input
protein_sequence = input("Enter protein sequence: ")

# Count the total number of amino acids in the protein sequence
num_amino_acids = len(protein_sequence)

# Count the number of non-protein amino acids in the sequence
non_protein_aa = protein_sequence.count('B') + protein_sequence.count('J') + \
                 protein_sequence.count('X') + protein_sequence.count('Z')

# Calculate the percentage of the sequence that is made up of proteins
percent_proteins = (num_amino_acids - non_protein_aa) / num_amino_acids * 100

# Print the results for protein sequence
print(f"Your protein sequence has {num_amino_acids} amino acids.")
print(f"The percentage of the sequence that is made up of proteins is {percent_proteins:.2f}%")

# Ask user for DNA sequence input
dna_sequence 
# Calculate the percentage of each nucleotide
total_nucleotides = len(dna_sequence)
nucleotide_percentages = {}
for nucleotide in nucleotide_counts:
    nucleotide_percentages[nucleotide] = (nucleotide_counts[nucleotide] / total_nucleotides) * 100

# Print the results for nucleotide frequencies
print("Nucleotide Counts:", nucleotide_counts)
print("Nucleotide Percentages:", nucleotide_percentages)= input("Enter DNA sequence: ")

# Count the number of each nucleotide
nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotide in dna_sequence:
    if nucleotide in nucleotide_counts:
        nucleotide_counts[nucleotide] += 1

