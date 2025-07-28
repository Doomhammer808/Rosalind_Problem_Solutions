def tree(filepath):
    '''
    Function for Rosalind problem 32: TREE
    (Completing a Tree)
    
    given a number x and pairs of nodes (nodes numbered from 1 to x)
    Return the minimum number of edges (connections)
    that can be added to produce a tree
    
    there will always be n-1 edges
    '''
    
    data = read_lines(filepath) # see problem 5
    limit = int(data[0])
    
    existing_edges = len(data)-1
    new_edges = limit-1-existing_edges
    
    return new_edges