def spliced_motif(filepath, output_file = 'output.txt'):
    '''
    Function for Rosalind problem 30: SSEQ
    (Finding a Spliced Motif)
    
    Given 2 DNA sequences
    return first indices in seq 1 where each successive letter of seq 2 appear
    '''
    
    sequences = read_fasta(filepath)[1] # see problem 5
    seq1 = sequences[0]
    seq2 = sequences[1]
    
    output = []
    
    ilook = 0
    just_added = 0
    for iletter in range(0,len(seq1)):
        if ilook == len(seq2):
            break
        
        if just_added:
            just_added = 0
            continue
        
        if seq1[iletter] == seq2[ilook]:
            output.append(iletter + 1)
            ilook += 1
            just_added = 1
    
    f = open(output_file, 'w')
    f.write(' '.join([str(x) for x in output]))
    f.close()
    
    print('Results written to output.txt')