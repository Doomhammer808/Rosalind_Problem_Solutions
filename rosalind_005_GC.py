def read_fasta(filepath):
    '''
    Function for reading FASTA files
    
    Returns 2 related lists, 1st with names, 2nd with sequences

    Really, most people use Biopython to read FASTA, but this is my own thing
    This function is gonna feature in a lot of following problems
    '''
    
    name_list = []
    seq_list = []
    n_lines = 0
    temp_seq = ''
    
    file = open(filepath, 'r')
    for line in file:
        n_lines += 1
        working_line = line.strip()
        #print(working_line)
        if working_line[0] == '>':
            if n_lines > 1:
                seq_list.append(temp_seq)       # assigning sequences
            temp_seq = ''
            name_list.append(working_line[1::]) # assigning names
        else:
            temp_seq = temp_seq + working_line
            
    seq_list.append(temp_seq)       # assigning final sequences
    
    file.close()
    
    return [name_list, seq_list]

###############################################################################
def gc_content(filepath):
    '''
    Function for Rosalind problem 5: GC (Computing GC Content)
    '''
    
    name_seq_list = read_fasta(filepath)
    gc_values = []
    for seq in name_seq_list[1]:
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        gc_values.append(round(gc, 6))
        
    target_index = gc_values.index(max(gc_values))
    print(name_seq_list[0][target_index], '\n', max(gc_values), sep='')