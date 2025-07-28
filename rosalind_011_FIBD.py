def rabbit_propagation_death(n_months, m_life):
    """
    Function for Rosalind problem 11: FIBD (Mortal Fibonacci Rabbits)

    n_months is the number of months that pass
    m_life is the number of months a rabbit lives
    
    Start with 1 pair. Only 1 pair produced per pair each month.
    Rabbits take 1 month to mature.
    So in 3 months a pair only reproduces twice.
    
    return number of total rabbit pairs still alive after n months
    """
    
    rabbit_counter = [0]*(m_life)
    # rabbit counter will keep count of generations of rabbits til death + new
    rabbit_counter[-1] = 1 #starting pair at immature
    print('month 1:', rabbit_counter)
    
    for i in range(n_months-1):
        rabbit_counter.append(sum(rabbit_counter[:-1])) # adding offspring
        rabbit_counter = rabbit_counter[1:] # killing the oldest generation
        print('month ', i+2, ': ', rabbit_counter, sep='')
        
    return sum(rabbit_counter)