def partial_permutations(n, k):
    '''
    Function for Rosalind problem 27: PPER
    (Partial Permutations)
    
    return N mod 1000 000 of possible permutations
    of length k using elements from n
    length k <= length n
    '''
    
    # there exists an established formula for this
    # n!/(n-k)!
    
    from math import factorial
    return int(factorial(n)/factorial(n-k) % 1000000)