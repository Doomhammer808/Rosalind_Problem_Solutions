def find_rflp_sites(filepath):
    '''
    Function for Rosalind problem 21: REVP (Locating Restriction Sites)
    
    return position and lengths of palindrome from 4 to 12bp in length
    '''
    
    sequence = read_fasta(filepath)[1][0]           # see problem 5
    alt_seq = reverse_complement(sequence)[::-1]    # see problem 3
    
    start_sites =[]
    lengths = []
    
    for istart in range(len(sequence)):
        prev_check = ''
        for check_length in range(4,13,2):
            check_seq = (sequence[istart:istart+check_length])
            if (len(check_seq) < 4 or check_seq == prev_check):
                break
            
            alt_check = alt_seq[istart: istart+check_length][::-1]
            
            if (check_seq == alt_check):
                start_sites.append(istart+1)
                lengths.append(check_length)
            
            prev_check = check_seq
    
    for i in range(len(start_sites)):
        print(start_sites[i], lengths[i])
