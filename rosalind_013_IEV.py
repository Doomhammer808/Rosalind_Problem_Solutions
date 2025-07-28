def expected_offspring(a, b, c, d, e, f):
    '''
    Function for Rosalind problem 13: IEV (Calculating Expected Offspring)
    
    a. AA-AA
    b. AA-Aa
    c. AA-aa
    d. Aa-Aa
    e. Aa-aa
    f. aa-aa
    
    These are the numbers of parent couples with specific genotypes
    Each couple has 2 kids
    
    Return the expected number of kids to have a dominant phenotype (AA or Aa)
    may return half a kid
    '''
    
    # chances
    # a. 100%
    # b. 100%
    # c. 100%
    # d. 75%
    # e. 50%
    # f. 0%      not important
    
    a_offspring = a*2
    b_offspring = b*2
    c_offspring = c*2
    d_offspring = d*2*0.75
    e_offspring = e*2*0.5
    
    n_dom = a_offspring + b_offspring + c_offspring + d_offspring + e_offspring
    
    return n_dom