def signed_permutations(n, output_file = 'output.txt'):
    '''
    Function for Rosalind problem 29: SIGN
    (Enumerating Oriented Gene Orderings)
    
    return permutations of a sequence, with negative number options too
    '''
    from itertools import permutations
    
    pos_seq = list(range(1,n+1))
    
    neg_seq = [-1*x for x in pos_seq]
    
    # I'm sure this is soooo inefficient
    # I'm creating a total permutations containing pos and neg numbers
    # then trimming down groups with a pos and neg of same number
    total_set = list(permutations(pos_seq + neg_seq, len(pos_seq)))
    
    output = []
    
    for group in total_set:
        group_check = 1
        for inum in range(0,len(pos_seq)):
            pos_num = pos_seq[inum]
            neg_num = neg_seq[inum]
            if pos_num in group and neg_num in group:
                group_check = 0
        if group_check:
            output.append(group)
    
    f = open(output_file, 'w')
    f.write(str(len(output)))
    for group in output:
        f.write('\n'+ ' '.join([str(x) for x in group]))
    f.close()
    
    print('Results written to', output_file)
