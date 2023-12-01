def translation(mRNA_sequence):

    codon = mRNA_sequence[:3]
    mRNA_sequence = mRNA_sequence[3:]
    return

def codon_to_amino_acid(codon):

    ##### Go through and properly merge the if elif statements
    # so that they are continous and do not have uneccessary number
    # of isolated if if if if statements on the same index line

    # enter depending on first base in codon ()
    if codon[0] == "U":

        # enters depending on second base in codon (U)
        if codon[1] == "U":

            # enters depending on third base in codon (UU)
            if codon[2] in ("U", "C"):
                return "PHE" # Phenylalanine
            elif codon[2] in ("A", "G"):
                return "LEU" # Leucine

        # enters depending on second base in codon (U)
        elif codon[1] == "C":
            return "SER" # Serine
        elif codon[1] == "A":

            # enters depending on third base in codon (UA)
            if codon[2] in ("U", "C"):
                return "TYR"  # Tyrosine
            elif codon[2] in ("A", "G"):
                return "STP" # Stop

        # enters depending on second base in codon (U)
        elif codon[1] == "G":

            # enters depending on third base in codon (UG)
            if codon[2] in ("U", "C"):
                return "CYS" # Cysteine
            elif codon[2] == "A":
                return "STOP" # Stop
            elif codon[2] == "G":
                return "TRP" # Tryptophan

    # enters depending on first base in codon ()
    elif codon[0] == "C":

        # enters depending on second base in codon (C)
        if codon[1] == "U":
            return "LEU" # Leucine
        elif codon[1] == "C":
            return "PRO" # Proline
        elif codon[1] == "A":

            # enters depending on third base in codon (CA)
            if codon[2] in ("U", "C"):
                return "HIS" # Histidine
            elif codon[2] in ("A", "G"):
                return "GLU" # Glutamine

        # enters depending on second base in codon (C)
        elif codon[1] == "G":
            return "ARG" # Arginine

    # enters depending on first base in codon ()
    elif codon[0] == "A":

        # enters depending on second base in codon (A)
        if codon[1] == "U":

            # enters depending on the third base in codon (AU)
            if codon[2] in ("U", "C", "A"):
                return "ILE" # Isoleucine
            elif codon[2] == "G":
                return "MET" # Methionine (Start)

        # enters depending on second base in codon (A)
        elif codon[1] == "C":
            return "THR" # Threonine
        elif codon[1] == "A":

            # enters depending on third base in codon (AA)
            if codon[2] in ("U", "C"):
                return "ASN" # Asparagine
            elif codon[2] in ("A", "G"):
                return "LYS" # Lysine

        # enters depending on second base in codon (A)
        elif codon[1] == "G":

            # enters depending on third base in codon (AG)
            if codon[2] in ("U", "C"):
                return "SER" # Serine
            elif codon[2] in ("A", "G"):
                return "ARG" # Arginine

    # enters depending on first base in codon ()
    elif codon[0] == "G":

        # enters depending on second base in codon (G)
        if codon[1] == "U":
            return "VAL" # Valine
        elif codon[1] == "C":
            return "ALA" # Alanine
        elif codon[1] == "A":

            # enters depending on third base in codon (GA)
            if codon[2] in ("U", "C"):
                return "ASP" # Aspartic Acid
            elif codon[2] in ("A", "G"):
                return "GLU" # Glutamic Acid

        # enters depending on second base in codon (G)
        elif codon[1] == "G":
            return "GLY" # Glycine
    return "ERR"

print(codon_to_amino_acid(["U","U","U"]))
translation(["U","U","U","U","U","U"])
