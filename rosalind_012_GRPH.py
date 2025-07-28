def edge_overlap(filepath, edge = 3):
    '''
    Function for Rosalind problem 12: GRPH (Overlap Graphs)
    
    returns pairs of sequence names with letter overlaps of a certain size
    where the first name has a suffix matching the prefix of the second name
    '''
    
    data = read_fasta(filepath) # see problem 5
    names = data[0]
    sequences = data[1]
    
    output_pairs = []
    
    for iseq in range(len(sequences)-1):
        seq1 = sequences[iseq]
        for jseq in range(iseq+1, len(sequences)):
            seq2 = sequences[jseq]
            if seq1[-edge:] == seq2[:edge] and seq1 != seq2:
                output_pairs.append([names[iseq], names[jseq]])
            if seq1[:edge] == seq2[-edge:] and seq1 != seq2:
                output_pairs.append([names[jseq], names[iseq]])
        
    print('total pairs:', len(output_pairs))
    for pair in output_pairs:
        print(pair[0], pair[1])