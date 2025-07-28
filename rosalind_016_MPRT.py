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
def get_url_lines(url):
    from urllib import request
    
    page = request.urlopen(url)
    output = page.readlines()
    for i in range(len(output)):
        output[i] = output[i].strip().decode('utf-8') # convert byte to string
        
    return output

###############################################################################
def locate_protein_motif(filepath):
    '''
    Function for Rosalind problem 16: MPRT (Finding a Protein Motif)
    
    takes file of uniprot protein ids
    accesses protein sequences online
    returns protein ids containing an N-glycosylation motif
    N[^P][ST][^P] = N + not P + S or T + not P
    '''
    
    import re
    
    proteins_list = read_lines(filepath)
    ref_list = []
    
    output = []
    
    for iprot in range(len(proteins_list)):
        ref_list.append(proteins_list[iprot].split('_')[0])
    
    for jprot in range(len(ref_list)):
        query_prot = ref_list[jprot]
        print('looking at protein', query_prot)
        url = ''.join(['https://rest.uniprot.org/uniprotkb/', 
                      query_prot, '.fasta'])
        prot_data = get_url_lines(url)
        prot_data = ''.join(prot_data[1:]) # protein sequence acquired
        
        matches = []
        
        pos = 0
        testing = True
        has_match = False
        
        while testing: # I hate using while
            index = re.search("N[^P][ST][^P]", prot_data[pos:])
            if index == None:
                testing = False
            else:
                has_match = True
                matches.append(index.start() + pos + 1)
                pos = matches[-1]
                matches[-1] = str(matches[-1])
                
        if has_match:
            output.append(proteins_list[jprot])
            output.append(matches)
        
    print('')
    for i in range (0, len(output)-1,2):
        print(output[i])
        print(' '.join(output[i+1]))