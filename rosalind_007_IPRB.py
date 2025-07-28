def prob_has_dom_allele(k, m, n):
    '''
    Function for Rosalind problem 7: IPRB (Mendel's First Law)
    
    k is the number of homozygous dominant
    m is the number of heterozygotes
    n is the number of homozygous recessive
    
    return chance that 2 random mates will produce an offspring
    with a dominant allele
    '''
    
    total = k+m+n
    # to get a dominant allele in offspring, options are
    # dominant mate with dominant, hetero or recessive (100%)
    # hetero mate with recessive (50%)
    # hetero mate with hetero (75%)
    # must minus one from total in the second multiplication
    # Therefore all probability calcs will have (x/total) * (x/total-1)
    # total * (total-1) becomes a common denominator
    denom = total * (total-1)
    
    # dominant mating chances
    dom_chance = k*(k-1) + k*m + k*n
    print(dom_chance/denom)
    
    # hetero chances
    het_chance = m*k + m*(m-1)*0.75 + m*n*0.5
    # note: k*m is duplicated from the dominant section because technically
    # the denominators would be different for each k or m (total or total-1)
    print(het_chance/denom)
    
    # recessive chances
    rec_chance = n*k + n*m*0.5
    print(rec_chance/denom)
    
    total_chance = (dom_chance + het_chance + rec_chance)/denom
    
    return round(total_chance, 6)