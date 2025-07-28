def splice_rna(filepath):
    '''
    Function for Rosalind problem 22: SPLC (RNA Splicing)
    
    return position and lengths of palindrome from 4 to 12bp in length
    '''
    
    data = read_fasta(filepath) # see problem 5
    
    seq = data[1][0]
    introns = data[1][1:]
    
    print(seq)
    
    for remove in introns:
        seq = seq.replace(remove, '')
    
    return translate_rna(seq)