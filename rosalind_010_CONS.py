def consensus_seq(filepath):
    '''
    Function for Rosalind problem 10: CONS (Consensus and Profile)

    Return a consensus sequence from a set of sequences
    and a matrix of nucleotide occurences
    '''
    
    sequences = read_fasta(filepath) # see problem 5
    sequences = sequences[1]
    seq_length = len(sequences[0])
    output_matrix = []
    
    for i in range(4):
        output_matrix.append([0]*seq_length)
    options = 'ACGT'
    
    # making matrix
    for seq in sequences:
        for iletter in range(seq_length):
            target_letter = seq[iletter]
            target_array = options.index(target_letter)
            
            output_matrix[target_array][iletter] += 1
    
    # making final sequence
    final_seq = ''
    for iletter in range(seq_length): # producing consensus sequence
        temp_list = []
        for j in range(4):
            temp_list.append(output_matrix[j][iletter])
            
        final_letter = options[temp_list.index(max(temp_list))]
        final_seq = final_seq + final_letter
    
    # output
    print(final_seq)
    for iarray in range(4):
        print(options[iarray]+':', *output_matrix[iarray], sep=' ')