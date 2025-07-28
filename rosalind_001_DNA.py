def count_nucleotides(seq):
    '''
    Function for Rosalind problem 1: DNA (Counting DNA Nucleotides)
    '''
    letter_counts = [0,0,0,0]
    letters_ref = 'ACGT'

    for i in range(4):
        for letter in seq:
            if letter.upper() == letters_ref[i]:
                letter_counts[i] = letter_counts[i] + 1

    print('\n')
    print (*letter_counts, sep=' ')