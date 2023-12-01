########################################################################################################################
#                                         Transcription / Translation area                                             #
########################################################################################################################



# inputs mRNA base pairs ["U", "A", "G"] returns amino acids as translated by a ribosome ["MET"]
def ribosome(mRNA_sequence):

    # holds variables for the translator to remember
    amino_acid_sequence = []
    amino_acid_index = 0
    MET_position = -1
    STP_position = -1

    # iterates through the indexes of the mRNA sequence 3 at a time until it has reached the end [0, 3, 6]
    for b in range(0, len(mRNA_sequence), 3):

        # saves calculation time if a stop codon is encountered
        if STP_position <= -1:

            # assigns the codon to three elements depending on the index of b->b+3
            # translates that through tRNA to an amino acid
            codon = mRNA_sequence[b:b+3]
            amino_acid = tRNA(codon)

            # check for start/stop codon and save their index
            if amino_acid == ["MET"]:
                MET_position = amino_acid_index
            if amino_acid == ["STP"]:
                STP_position = amino_acid_index
            amino_acid_index += 1

            # If MET codon found, transcribe current codon
            if MET_position > -1:
                amino_acid_sequence.extend(amino_acid)

    # return amino acid sequence once all codons have been translated
    return amino_acid_sequence



# inputs mRNA ["U", "U", "U"] outputs amino acids ["MET"]
def tRNA(codon):

    # try statement to avoid errors if there is not enough bases in the codon
    try:

        # enter depending on first base in codon ()
        if codon[0] == "U":

            # enters depending on second base in codon (U)
            if codon[1] == "U":

                # enters depending on third base in codon (UU)
                if codon[2] in ("U", "C"):
                    return ["PHE"]  # Phenylalanine
                elif codon[2] in ("A", "G"):
                    return ["LEU"]  # Leucine

            # enters depending on second base in codon (U)
            elif codon[1] == "C":
                return ["SER"]  # Serine
            elif codon[1] == "A":

                # enters depending on third base in codon (UA)
                if codon[2] in ("U", "C"):
                    return ["TYR"]  # Tyrosine
                elif codon[2] in ("A", "G"):
                    return ["STP"]  # Stop

            # enters depending on second base in codon (U)
            elif codon[1] == "G":

                # enters depending on third base in codon (UG)
                if codon[2] in ("U", "C"):
                    return ["CYS"]  # Cysteine
                elif codon[2] == "A":
                    return ["STP"]  # Stop
                elif codon[2] == "G":
                    return ["TRP"]  # Tryptophan

        # enters depending on first base in codon ()
        elif codon[0] == "C":

            # enters depending on second base in codon (C)
            if codon[1] == "U":
                return ["LEU"]  # Leucine
            elif codon[1] == "C":
                return ["PRO"]  # Proline
            elif codon[1] == "A":

                # enters depending on third base in codon (CA)
                if codon[2] in ("U", "C"):
                    return ["HIS"]  # Histidine
                elif codon[2] in ("A", "G"):
                    return ["GLU"]  # Glutamine

            # enters depending on second base in codon (C)
            elif codon[1] == "G":
                return ["ARG"]  # Arginine

        # enters depending on first base in codon ()
        elif codon[0] == "A":

            # enters depending on second base in codon (A)
            if codon[1] == "U":

                # enters depending on the third base in codon (AU)
                if codon[2] in ("U", "C", "A"):
                    return ["ILE"]  # Isoleucine
                elif codon[2] == "G":
                    return ["MET"]  # Methionine (Start)

            # enters depending on second base in codon (A)
            elif codon[1] == "C":
                return ["THR"]  # Threonine
            elif codon[1] == "A":

                # enters depending on third base in codon (AA)
                if codon[2] in ("U", "C"):
                    return ["ASN"]  # Asparagine
                elif codon[2] in ("A", "G"):
                    return ["LYS"]  # Lysine

            # enters depending on second base in codon (A)
            elif codon[1] == "G":

                # enters depending on third base in codon (AG)
                if codon[2] in ("U", "C"):
                    return ["SER"]  # Serine
                elif codon[2] in ("A", "G"):
                    return ["ARG"]  # Arginine

        # enters depending on first base in codon ()
        elif codon[0] == "G":

            # enters depending on second base in codon (G)
            if codon[1] == "U":
                return ["VAL"]  # Valine
            elif codon[1] == "C":
                return ["ALA"]  # Alanine
            elif codon[1] == "A":

                # enters depending on third base in codon (GA)
                if codon[2] in ("U", "C"):
                    return ["ASP"]  # Aspartic Acid
                elif codon[2] in ("A", "G"):
                    return ["GLU"]  # Glutamic Acid

            # enters depending on second base in codon (G)
            elif codon[1] == "G":
                return ["GLY"]  # Glycine

    # if there is not enough base pairs in the codon, handle the error
    except IndexError:
        return ["ERR"]



# translates DNA to mRNA
def mRNA_polymerase():
    return



print(ribosome(["A","A","A","A","U","G","C","U","C","U","A","G","A","A","A","A"]))