def get_length(dna):
    return len(dna)


def is_longer(dna1, dna2):
    if get_length(dna1)<get_length(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    for char in dna:
        count=0
        if char==nucleotide:
            count+=1
    return count


def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    for char in dna:
        sequence=['A','T','G','C']
        if char != sequence:
            return False
        else:
            return False
    return 0

def insert_sequence(dna1,dna2,index):
    result=dna1[:index]+dna2+dna1[index:]
    return result

def get_complement():
    return 0
def get_complementary_sequence():
    return 0