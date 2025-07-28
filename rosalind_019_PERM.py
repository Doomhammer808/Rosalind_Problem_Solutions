def count_permutations(number):
    '''
    Function for Rosalind problem 19: PERM (Enumerating Gene Orders)
    
    given a number, return number of and the possible permutations of
    0 -> the given number
    '''
    
    from itertools import permutations
    
    reference = list(range(1, number+1))
    perms = list(permutations(reference))
    
    # too much data for the iPython buffer window
    # create a separate output file
    f = open("output.txt", "w")
    f.write(str(len(perms))+'\n')
    for i in perms:
        f.write(' '.join(str(x) for x in i)+'\n')
    f.close()
    
    print('results written to output.txt')