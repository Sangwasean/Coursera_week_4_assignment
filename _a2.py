def get_length(dna):
    print(len(dna))
    return len(dna)

def is_longer(dna1, dna2):
    if get_length(dna1)>get_length(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    count = 0
    for char in dna:
        if char==nucleotide:
            count+=1
    return count


def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    Boolean=True
    sequence=['A','T','G','C']
    for char in dna:
        if char in sequence:
            Boolean=True
        else:
            Boolean=False
            break
    return (Boolean)

def insert_sequence(dna1,dna2,index):
    result=dna1[:index]+dna2+dna1[index:]
    return result

def get_complement(nucleotide):
    result=''
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for char in nucleotide:
        result = complement_map.get(nucleotide)
    return  result


def get_complementary_sequence(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result=''
    for char in dna:
        complement = get_complement(char)
        result+=complement
    return(result)