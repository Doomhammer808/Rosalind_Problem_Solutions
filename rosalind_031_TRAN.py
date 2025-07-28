def tran(filepath):
    '''
    Function for Rosalind problem 31: TRAN
    (Transitions and Transversions)
    
    2 DNA seqs with same lengths
    return transition/transversion ratio

    Hamming Distance = number of mutations/substitutions/differing letters
    Transition = purine to purine (A<->G)/pyrimidine to pyrimidine (C<->T)
    Transversion = purine to pyrimidine or vice versa (A/G <-> C/T)
    '''
    
    sequences = read_fasta(filepath)[1] # see problem 5
    seq1 = sequences[0]
    seq2 = sequences[1]
    
    n_transitions = 0
    n_transversions = 0
    
    from pandas import DataFrame
    # gonna use this table for determining transitions/transversions
    ref_frame = DataFrame([
    [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    ['A','G','C','T'],
    ['A','G','C','T'])
    
    for i in range(0, len(seq1)):
        letter1 = seq1[i]
        letter2 = seq2[i]
        if letter1 != letter2:
            if ref_frame.loc[letter1][letter2]:
                n_transitions += 1
            else:
                n_transversions += 1
    
    return(n_transitions/n_transversions)