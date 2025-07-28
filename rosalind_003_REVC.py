def reverse_complement(seq):
    '''
    Function for Rosalind problem 3: REVC (Complementing a Strand of DNA)
    '''
    original_ref = 'ATCG'
    complement_ref = 'TAGC'
    new_string = ''
    
    for letter in seq:
        target = original_ref.index(letter)
        new_string = new_string + complement_ref[target]
    
    return(new_string[::-1])