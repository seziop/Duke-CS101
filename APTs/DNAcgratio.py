def ratio(dna):
    number_of_c = dna.count('c')
    number_of_g = dna.count('g')
    number_of_all=len(dna)
    return (number_of_c+number_of_g)/number_of_all