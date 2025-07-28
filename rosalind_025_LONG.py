def superstring(filepath, write_out = True, out_file = 'output.txt'):
    '''
    Function for Rosalind problem 25: LONG (Genome Assembly as Shortest Superstring)
    '''
    
    # sequences = read_fasta('input.txt')[1]
    sequences = read_fasta(filepath)[1]
    
    master_seq = sequences[0]
    added = [1]+([0]*(len(sequences)-1))
    
    for iseq in range(1, len(sequences)): # repeatedly run through all seq
        for jseq in range(1, len(sequences)): # for each seq, compare
            check_seq = sequences[jseq]
            #print(check_seq)
            
            # look for match starting from half
            half_len = round(len(check_seq)/2)
            
            front_added = 0
            back_added = 0
            
            if not added[jseq]:
                # checking on to backend of master sequence
                for bp in range(half_len, len(check_seq)):
                    partial = check_seq[0:bp]
                    #print(partial)
                    if partial == master_seq[-bp:]:
                        master_seq = master_seq + check_seq[bp:]
                        back_added = 1
                        
                        #print('sequence',jseq-1,'added to back')
                        
                        added[jseq] = 1
                        break
                
                # checking on to frontend of master sequence
                for bp in range(0, half_len)[::-1]:
                    partial = check_seq[bp:]
                    #print(partial)
                    
                    if partial == master_seq[:len(partial)]:
                        master_seq = check_seq[:bp] + master_seq
                        front_added = 1
                        
                        #print('sequence',jseq-1,'added to front')
                        
                        added[jseq] = 1
                
                if front_added and back_added:
                    print('Warning: front and back matches for sequence',
                          iseq+1)
    
    if not write_out:
        return master_seq
    else:
        f = open(out_file, 'w')
        f.write(master_seq)
        f.close()
        print('Results written to', out_file)