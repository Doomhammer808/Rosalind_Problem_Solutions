def read_lines(filepath):
    '''
    Function for reading lines into a list from a file
    '''
    
    output = []
    
    file = open(filepath, 'r')
    for line in file:
        output.append(line.strip())
    
    file.close()
    
    return output

###############################################################################
def prob_with_gc(filepath):
    '''
    Function for Rosalind problem 28: PROB
    (Introduction to Random Strings)
    
    line 1 of the file contains a DNA sequence
    line 2 contains theoretical constants for gc content
    
    given a gc content, what is the probability of a random DNA string
    matching the original?
    Result reported as log10(probability) as the numbers are very small.
    
    (Is this really accurate to the order of the letters?)
    '''
    
    from math import log10
    
    output = []
    
    f = read_lines(filepath) # see problem 3
    seq = f[0]
    gc_content = [float(x) for x in f[1].split()]
    
    for gc in gc_content:
        pgc =gc/2
        pat = (1-gc)/2
        prob = 1
        
        for letter in seq:
            if letter in 'ATU':
                prob = prob*pat
            if letter in 'GC':
                prob = prob*pgc
        
        output.append(round(log10(prob), 3))
    
    print(' '.join(['%.3f' % z for z in output]))
    return output