def prob_hetero_in_kth_gen(k_gen = 2, n_hets = 1):
    '''
    Function for Rosalind problem 15: LIA (Independent Alleles)
    
    return probability that at least n_hets exist in kth generation
    progenitor is AaBb in 0th gen, all mates are AaBb, and they have 2 kids
    '''
    
    # chance of hetero with AaBb x AaBb = 25%
    # law of independent assortment dictates that
    # chance of Aa x Bb = chance of AaBb (1/2 x 1/2 = 1/4)
    # =========================================================================
    #   	AB      Ab	    aB	    ab
    # AB	AABB	AABb	AaBB	AaBb*
    # Ab	AABb	AAbb	AaBb*	Aabb
    # aB	AaBB	AaBb*	aaBB	aaBb
    # ab	AaBb*	Aabb	aaBb	aabb
    # =========================================================================
    #
    # for probabilities, we measure failure, not successes, so 1 - answer
    
    # 2**k trials/generations due to 2 kids over certain number of generations
    # P(N successes) = P(2**k - N failures)
    # these probabilities for a binomial distribution
    # cdf is a common binomial distribution function
    
    # in scipy cdf arguments are
    # k desired successes (upper limit) We want a lower limit, so minus 1
    # e.g. want 3 or more successes, ask cdf for chance of 2 (0, 1, or 2).
    # then (1-final answer) for probability of 3 or more
    # n number of trials
    # p probability of success in one trial
    
    from scipy import stats
    
    return 1-stats.binom.cdf(n_hets - 1, 2**k_gen, 0.25)