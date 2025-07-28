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
def longest_subseq(filepath):
    '''
    Function for Rosalind problem 24: LGIS (Longest Increasing Subsequence)
    
    Given a number and a permutation of a number sequence up to this number
    E.g.
    5
    5 4 1 3 2
    
    We want to return the longest increasing subsequence (1 2)
    And the longest decreasing subsequence (5 4 3 2)
    
    Easy for a small number, but efficiency becomes a serious problem with
    large numbers
    
    Need to learn the Patience Sorting algorithm.
    
    Uses lis() and lds() defined below this function
    '''
    data = read_lines(filepath)
    seq = data[1].split()
    seq = [int(x) for x in seq] # comparisons must be in int
    longest_inc = lis(seq)
    longest_dec = lds(seq)
    
        
    f = open('output.txt', 'w')
    f.write(' '.join(str(x) for x in longest_inc)+'\n')
    f.write(' '.join(str(x) for x in longest_dec))
    f.close()
    
    print(' '.join(str(x) for x in longest_inc)+'\n')
    print(' '.join(str(x) for x in longest_dec)+'\n')
    print('results written to output.txt')



def lis(seq):
    '''
    return longest increasing subsequence given a list of numbers
    '''
    
    # test sequences
    # x = [10,9,2,5,3,7,101,18]
    # y = [5,10,2,3,7,14,28,4,9,12,8,21]
    
    # "Whenever a card is placed on top of a pile, put a back-pointer to the
    # top card in the previous pile (that, by assumption, has a lower value
    # than the new card has). In the end, follow the back-pointers from the
    # top card in the last pile to recover a decreasing subsequence of the
    # longest length; its reverse is an answer to the longest increasing
    # subsequence algorithm"
    
    stacks = [[seq[0]]]
    traceback_dict = {}
    for i in range(1,len(seq)):
        number = seq[i]
        istack = -1
        added = 0
        
        for stack in stacks:
            istack += 1
            if stack[-1] > number:
                stack.append(number) #placing number on left most option
                added = 1
                break
                
        if not added:
            istack += 1
            stacks.append([number]) # make new stack
        
        if istack > 0:
            traceback_dict[number] = stacks[istack-1][-1]
            # linking to last stack
    
    # construct sequence
    output = [stacks[-1][-1]]  # Longest possible sequence = number of stacks
    looking_for = stacks[-1][-1]
    keys = traceback_dict.keys()
    
    while looking_for in keys:
        looking_for = traceback_dict[looking_for]
        output.append(looking_for)
        # assembling from highest to lowest
    
    # print('n stacks:', len(stacks))
    # print('n subseq:', len(output))
    
    return output[::-1]

def lds(array):
    """
    return longest decreasing subsequence given a list of numbers

    uses negative numbers and the lis() function
    with negatives, the smallest become biggest and vice versa
    """
    
    negated_arr = [-int(number) for number in array]
    lds_negated = lis(negated_arr)
    output = [-x for x in lds_negated]
    return output