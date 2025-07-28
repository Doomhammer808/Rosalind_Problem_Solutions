def lexicographic_permutations(alphabet, length):
    '''
    Function for Rosalind problem 23: LEXF (Enumerating k-mers Lexicographically)
    
    Given a list of symbols
    return all possible strings using these with the given length
    
    E.g.
    ABC, 3 =
    AAA
    AAB
    AAC
    ABA
    ABB
    etc.
    '''
    
    from itertools import product # this function literally does this job
    
    output_list = list(product(alphabet.replace(' ',''), repeat=length))
    f = open('output.txt', 'w')
    for i in output_list:
        f.write(''.join(i)+'\n')
    f.close()
    print('results written to output.txt')