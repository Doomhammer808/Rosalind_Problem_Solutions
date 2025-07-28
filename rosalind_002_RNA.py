def replace_letter(seq, t = 'T', u = 'U'):
    '''
    Function for Rosalind problem 2: RNA (Transcribing DNA into RNA)
    '''
    new_string = ''
    for letter in seq:
        if letter == t:
            new_string = new_string + u
        else:
            new_string = new_string + letter
    
    # print('\n'+new_string)
    return(new_string)