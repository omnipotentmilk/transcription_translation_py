import random

########################################################################################################################
#                                         Transcription / Translation area                                             #
########################################################################################################################



# inputs mRNA base pairs ["A", "U", "G"] returns amino acids as translated by a ribosome ["MET"]
def ribosome(mRNA_sequence):

    # initialize vars
    amino_acid_sequence = []
    MET_position = -1

    # Find the position of the start codon "AUG", pass if there are no more amino acids to properly index
    try:
        for i in range(len(mRNA_sequence) - 2):
            if mRNA_sequence[i:i + 3] == ["A", "U", "G"]:
                MET_position = i
                break

    # if loop encounter an index error, the mRNA is non coding
    except IndexError:
        return []

    # read only if MET has been found
    if MET_position > -1:

        # iterates though mRNA from the MET_position to the end
        for i in range(MET_position, len(mRNA_sequence), 3):

            # grab 3 bases and translate them
            codon = mRNA_sequence[i:i+3]
            amino_acid = tRNA(codon)

            # Check for stop codon; break if found, append amino acids if not
            if amino_acid == "STP":
                break
            else:
                amino_acid_sequence.append(amino_acid)

    # if MET_position was never found
    else:
        return []

    # if translation has completed
    return amino_acid_sequence


# mRNA codon is ["A", "U", "G"], amino acid is ["MET"]
def tRNA(codon):

    # try statement to avoid errors if there is not enough bases in the codon
    try:

        # enter depending on first base in codon ()
        if codon[0] == "U":

            # enters depending on second base in codon (U)
            if codon[1] == "U":

                # enters depending on third base in codon (UU)
                if codon[2] in ("U", "C"):
                    return "PHE"  # Phenylalanine
                elif codon[2] in ("A", "G"):
                    return "LEU"  # Leucine

            # enters depending on second base in codon (U)
            elif codon[1] == "C":
                return "SER"  # Serine
            elif codon[1] == "A":

                # enters depending on third base in codon (UA)
                if codon[2] in ("U", "C"):
                    return "TYR"  # Tyrosine
                elif codon[2] in ("A", "G"):
                    return "STP"  # Stop

            # enters depending on second base in codon (U)
            elif codon[1] == "G":

                # enters depending on third base in codon (UG)
                if codon[2] in ("U", "C"):
                    return "CYS"  # Cysteine
                elif codon[2] == "A":
                    return "STP"  # Stop
                elif codon[2] == "G":
                    return "TRP"  # Tryptophan

        # enters depending on first base in codon ()
        elif codon[0] == "C":

            # enters depending on second base in codon (C)
            if codon[1] == "U":
                return "LEU"  # Leucine
            elif codon[1] == "C":
                return "PRO"  # Proline
            elif codon[1] == "A":

                # enters depending on third base in codon (CA)
                if codon[2] in ("U", "C"):
                    return "HIS"  # Histidine
                elif codon[2] in ("A", "G"):
                    return "GLU"  # Glutamine

            # enters depending on second base in codon (C)
            elif codon[1] == "G":
                return "ARG"  # Arginine

        # enters depending on first base in codon ()
        elif codon[0] == "A":

            # enters depending on second base in codon (A)
            if codon[1] == "U":

                # enters depending on the third base in codon (AU)
                if codon[2] in ("U", "C", "A"):
                    return "ILE"  # Isoleucine
                elif codon[2] == "G":
                    return "MET"  # Methionine (Start)

            # enters depending on second base in codon (A)
            elif codon[1] == "C":
                return "THR"  # Threonine
            elif codon[1] == "A":

                # enters depending on third base in codon (AA)
                if codon[2] in ("U", "C"):
                    return "ASN"  # Asparagine
                elif codon[2] in ("A", "G"):
                    return "LYS"  # Lysine

            # enters depending on second base in codon (A)
            elif codon[1] == "G":

                # enters depending on third base in codon (AG)
                if codon[2] in ("U", "C"):
                    return "SER"  # Serine
                elif codon[2] in ("A", "G"):
                    return "ARG"  # Arginine

        # enters depending on first base in codon ()
        elif codon[0] == "G":

            # enters depending on second base in codon (G)
            if codon[1] == "U":
                return "VAL"  # Valine
            elif codon[1] == "C":
                return "ALA"  # Alanine
            elif codon[1] == "A":

                # enters depending on third base in codon (GA)
                if codon[2] in ("U", "C"):
                    return "ASP"  # Aspartic Acid
                elif codon[2] in ("A", "G"):
                    return "GLU"  # Glutamic Acid

            # enters depending on second base in codon (G)
            elif codon[1] == "G":
                return "GLY"  # Glycine

    # if there is not enough base pairs in the codon, handle the error
    except IndexError:
        return "ERR" # handles unknown mutations



# translates DNA to mRNA
# if DNA is ["T","A","C"], mRNA is ["A","U","G"]
def mRNA_polymerase(DNA_Sequeence):

    mRNA_sequence = []
    for b in DNA_Sequeence:
        if b == "T": # turns to A
            b = "A"
        elif b == "C": # turns to G
            b = "G"
        elif b == "A": # turns to U
            b = "U"
        elif b == "G": # turns to C
            b = "G"
        else:
            b = "E" # handles unknown mutations
        mRNA_sequence.append(b)

    return mRNA_sequence



# converts an artifical genome (0123) to DNA base pairs (AGTC)
def DNA_Polymerase(artifical_genome):

    # create empty DNA sequence
    DNA_Sequeence = []

    # convert artifical genome to base pairs
    for d in artifical_genome:
        if d == 0:
            DNA_Sequeence.append("A")
        elif d == 1:
            DNA_Sequeence.append("G")
        elif d == 2:
            DNA_Sequeence.append("T")
        elif d == 3:
            DNA_Sequeence.append("C")

    # return converted list
    return DNA_Sequeence



# generates an artifical genome using player inputs
def LAB_Polymerase():

    # initialize vars
    nested_LAB_genome = []

    # enters a while loop to avoid input errors
    while True:
        try:

            # prompts for strand length & count
            number_of_strands = int(input("How many strands of LAB genome would you like to create? "))
            LAB_sequence_length = int(input("How long should each LAB genome be? "))

            # creates strands based on specificed length
            for n in range(number_of_strands):
                random_num_sequence = random.choices(range(0, 4), k=LAB_sequence_length)
                nested_LAB_genome.append(random_num_sequence)
            break

        # handles input errors
        except ValueError:
            print("Please enter a valid integer next time.")

    # returns genome after the function has finished
    return nested_LAB_genome

nested_polypeptide = []
output = LAB_Polymerase()
for n in output:
    nested_polypeptide.append(ribosome(mRNA_polymerase(DNA_Polymerase(n))))

for _ in range(len(nested_polypeptide)):
    print(len(nested_polypeptide[_]))