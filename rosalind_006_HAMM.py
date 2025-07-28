def count_differences(seq1, seq2):
    '''
    Function for Rosalind problem 6: HAMM (Counting Point Mutations)
    '''
    mutation_count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutation_count += 1
    
    return mutation_count