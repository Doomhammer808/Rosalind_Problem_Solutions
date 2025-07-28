def index_motif(seq, motif):
    '''
    Function for Rosalind problem 9: SUBS (Finding a Motif in DNA)
    '''
    
    i = 0
    output_indices = []
    for letter in seq:
        if letter == motif[0] and not i+len(motif) > len(seq):
            # print('checking', i)
            if seq[i:i+len(motif)] == motif:
                output_indices.append(i+1)
                # note we are returning position
                # not python index
        i += 1
    
    print(' '.join(str(b) for b in output_indices))