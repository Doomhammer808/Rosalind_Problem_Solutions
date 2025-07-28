def rabbit_propagation(n_months, k_pairs):
    """
    Function for Rosalind problem 4: FIB (Rabbits and Recurrence Relations)

    n_months is the number of months that pass

    k_pairs is the number of rabbit pairs produced by each existing pair from
    the previous month. Start with 1 pair. rabbits take 1 month to mature.

    Note that the number of offspring in any month is equal to the number of
    rabbits that were alive two months prior
    
    A month only contains the rabbits from the previous month
    plus the new offspring. The older generations die.
    
    supposed to use Fibonacci sequence, but screw it.
    
    return number of mature breeding pairs after n months

    """
    parents = 1
    immature = 0
    offspring = 0
    
    for i in range(n_months): # we are looking at the nth month,
                                # not letting it complete

        # these print statments are just for visualising the process
        print('At the start of month', i+1, ':')
        print('parents', '\t', 'immature', '\t', 'offspring')
        print(parents, '\t', immature, '\t', offspring)
        print('')
        
        if (i != n_months-1):
            offspring = parents * k_pairs
            parents = parents + immature # each category moves up one
            immature = offspring
        else:
            return parents