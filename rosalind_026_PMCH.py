def rna_perfect_matches(filepath):
    '''
    Function for Rosalind problem 26: PMCH
    (Perfect Matchings and RNA Secondary Structures)
    
    Input sequence has nA = nU and nG = nC
    '''
    
    from math import factorial
    
    sequence = read_fasta(filepath)[1][0]
    print(sequence)
    
    # functionally, the matchings between A-U and G-C are independent
    AU = 0
    GC = 0
    
    # because the first "node" can connect to n-1 other nodes
    # and then the next can connect to n-2
    # etc
    # we essentially get a factorial function for the number of perfect matches
    # E.g. n=5; 5! = 5*4*3*2*1
    
    for letter in sequence:
        if letter == 'A':
            AU += 1
        if letter == 'G':
            GC += 1
    
    answer = factorial(AU) * factorial(GC)
    
    return answer