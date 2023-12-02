import random

########################################################################################################################
#                                         Transcription / Translation area                                             #
########################################################################################################################



########################################################################################################################
#                                           modify this to be cleaner                                                  #

# inputs mRNA base pairs ["A", "U", "G"] returns amino acids as translated by a ribosome ["MET"]
def ribosome(mRNA_sequence):

    # Find the position of the start codon "AUG", return if there are no more amino acids to properly index
    try:
        MET_position = -1
        for i in range(len(mRNA_sequence) - 2):
            if mRNA_sequence[i:i + 3] == ["A", "U", "G"]:
                MET_position = i
                break
    except IndexError:
        return []

    # iterates from the MET_position to end. return sequence when finished.
    amino_acid_sequence = []
    for i in range(MET_position, len(mRNA_sequence), 3):

        # grab 3 bases and translate them
        codon = mRNA_sequence[i:i+3]
        amino_acid = tRNA(codon)

        # Check for stop codon; break if found, append amino acids if not.
        if amino_acid == "STP":
            break
        elif amino_acid == "ERR":
            pass
        else:
            amino_acid_sequence.append(amino_acid)
    return amino_acid_sequence

#                                           modify this to be cleaner                                                  #
########################################################################################################################



# mRNA codon is ["A", "U", "G"], amino acid is ["MET"]
def tRNA(codon):

    # lookup dict containing all corresponding amino acid sequences
    codon_table = {
        "UUU": "PHE", "UUC": "PHE",
        "UUA": "LEU", "UUG": "LEU", "CUU": "LEU", "CUC": "LEU", "CUA": "LEU", "CUG": "LEU",
        "UCU": "SER", "UCC": "SER", "UCA": "SER", "UCG": "SER",
        "UAU": "TYR", "UAC": "TYR", "UAA": "STP", "UAG": "STP",
        "UGU": "CYS", "UGC": "CYS", "UGA": "STP", "UGG": "TRP",
        "CUU": "LEU", "CUC": "LEU", "CUA": "LEU", "CUG": "LEU",
        "CCU": "PRO", "CCC": "PRO", "CCA": "PRO", "CCG": "PRO",
        "CAU": "HIS", "CAC": "HIS", "CAA": "GLU", "CAG": "GLU",
        "CGU": "ARG", "CGC": "ARG", "CGA": "ARG", "CGG": "ARG",
        "AUU": "ILE", "AUC": "ILE", "AUA": "ILE", "AUG": "MET",
        "ACU": "THR", "ACC": "THR", "ACA": "THR", "ACG": "THR",
        "AAU": "ASN", "AAC": "ASN", "AAA": "LYS", "AAG": "LYS",
        "AGU": "SER", "AGC": "SER", "AGA": "ARG", "AGG": "ARG",
        "GUU": "VAL", "GUC": "VAL", "GUA": "VAL", "GUG": "VAL",
        "GCU": "ALA", "GCC": "ALA", "GCA": "ALA", "GCG": "ALA",
        "GAU": "ASP", "GAC": "ASP", "GAA": "GLU", "GAG": "GLU",
        "GGU": "GLY", "GGC": "GLY", "GGA": "GLY", "GGG": "GLY",
    }

    # return a join version of the codon, ERR if not found
    return codon_table.get("".join(codon), "ERR")



# translates DNA to mRNA
# if DNA is ["T","A","C"], mRNA is ["A","U","G"]
def mRNA_polymerase(DNA_Sequence):

    # mapping DNA to mRNA bases
    mapping = {"T": "A", "C": "G", "A": "U", "G": "C", "E": "E"}

    # iterates through DNA and maps it to mRNA
    mRNA_sequence = [mapping[m] for m in DNA_Sequence]

    # return translated mRNA
    return mRNA_sequence



# possibly temporary function, when given a DNA sequence, converts either point or frame shift mutations at a random
# point in the DNA genome
def DNA_mutation_factor(DNA_Sequence, num_iterations=3):

    # assumes each codon is 300 base pairs long
    deletion_chance = 0.65
    insertion_chance = 0.4
    substitution_chance = 0.95

    # by default produces 6 mutations
    for _ in range(num_iterations):
        # Check for deletion
        if random.random() < deletion_chance:
            delete_position = random.randint(0, len(DNA_Sequence) - 1)
            del DNA_Sequence[delete_position]

        # Check for insertion
        if random.random() < insertion_chance:
            insert_position = random.randint(0, len(DNA_Sequence))
            inserted_base = random.choice(["A", "G", "T", "C"])
            DNA_Sequence.insert(insert_position, inserted_base)

        # Check for substitution
        if random.random() < substitution_chance:
            substitute_position = random.randint(0, len(DNA_Sequence) - 1)
            substituted_base = random.choice(["A", "G", "T", "C"])
            DNA_Sequence[substitute_position] = substituted_base

    # returns mutated sequence
    return DNA_Sequence



# converts an artifical genome (0123) to DNA base pairs (AGTC)
def DNA_Polymerase(artificial_genome):

    # maps artificial genome values to DNA base pairs
    mapping = {0: "A", 1: "G", 2: "T", 3: "C", 4: "E"}

    # iterates through artifical genome and converts to DNA base pairs
    DNA_Sequence = [mapping[d] for d in artificial_genome]

    # Return dna genome
    return DNA_Sequence

########################################################################################################################
#                                                   modify to be clean                                                 #

# generates an artifical genome using player inputs
def LAB_Polymerase():

    # initialize vars
    nested_LAB_genome = []

    # enters a while loop to avoid input errors
    while True:
        try:

            # prompts for strand length & count
            number_of_strands = int(input("How many strands of LAB genome would you like to create? "))
            LAB_sequence_length = 300 #int(input("How long should each LAB genome be? "))

            # creates strands based on specificed length
            for n in range(number_of_strands):
                random_num_sequence = random.choices(range(0, 4), k=LAB_sequence_length)
                nested_LAB_genome.append(random_num_sequence)

            # notifies user that their artifical genome has finished generating
            print("Finished generating sequences, sending to cell.")
            break

        # handles input errors
        except ValueError:
            print("Please enter a valid integer next time.")

    # returns genome after the function has finished
    return nested_LAB_genome



# outputs useful information regarding genomes
def UXUI():

    # holds outputs to be displayed
    nested_polypeptide = []
    polypepte_length = []
    output = LAB_Polymerase()

    # iterates through every amino acid sequence generated and appends it to a nested list with variable index
    for n in output:
        nested_polypeptide.append(ribosome(mRNA_polymerase(DNA_Polymerase(n))))

    # finds the length of each polypeptide in the nested polypeptide list
    for _ in range(len(nested_polypeptide)):
        polypepte_length.append(len(nested_polypeptide[_]))

    # displays the average length
    print(f"average peptide length is {sum(polypepte_length)/len(polypepte_length)}")
    print(nested_polypeptide[0])
    return

#                                           modify this to be cleaner                                                  #
########################################################################################################################


UXUI()


# golgi apperatus