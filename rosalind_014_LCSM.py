def longest_common_substr(filepath):
    '''
    Function for Rosalind problem 14: LCSM (Finding a Shared Motif)
    '''
    
    data = read_fasta(filepath) # see problem 5
    
    sequences = data[1]
    seq1 = sequences[0]
    common = ''
    
    for check_length in range(len(seq1),0,-1):
        # sizes to check, starting from biggest
        for istart in range(len(seq1)): #starting pos to 1st seq to check from
            if istart + check_length > len(seq1):
                break # stop if seq to check greater than reference
            else:
                query_seq = seq1[istart:istart + check_length]
                for check_seq in sequences[1:]: # look for seq in others
                    if query_seq not in check_seq:
                        common = ''
                        break # move onto next checking seq if not in any other
                    else:
                        common = query_seq
                if common != '': # checking if it made it through all sequences
                    return common