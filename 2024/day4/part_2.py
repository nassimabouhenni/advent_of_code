# Day 4 Part 1 

import re

with open("advent_of_code_2024_04.txt", "r") as file:
    text = file.read()

text_split = text.split("\n")
n = len(text_split) # assume square grid
sequence = [i for i in range(n)] # get possible sequences, assume square grid

##########################

# text read diagonal (L-R, down)


# 9,89,789,etc
a_sequence_expanded = []
for i in range(n-1):
    a_sequence_expanded.append(sequence[n-(i+1):n])

for i in range(n-1):
    a_sequence_expanded.append(sequence[0:n-(i)])
    
# 0,01,012,etc
b_sequence_expanded = []
for i in range(n-1):
    b_sequence_expanded.append(sequence[0:i+1])

for i in range(n-1):
    b_sequence_expanded.append(sequence[i:n])
    
# 9,98,987,etc
c_sequence_expanded = []
for i in range(n-1):
    c_sequence_expanded.append(sequence[n-(i+1):n][::-1])

for i in range(n-1):
    c_sequence_expanded.append(sequence[0:n-(i)][::-1])

# 0,10,210,etc    
d_sequence_expanded = []
for i in range(n-1):
    d_sequence_expanded.append(sequence[0:i+1][::-1])

for i in range(n-1):
    d_sequence_expanded.append(sequence[i:n][::-1])
    

# Select sequences based on diag type
def sequence_generator(seq1, seq2):
    text = []
    for list1,list2 in zip(seq1,seq2):
        row = ""
        for x,y in zip(list1,list2):
            row = row + text_split[x][y]
        text.append(row)
    return text

def coord_mapper(seq1, seq2):
    mapping = {}
    i = 0
    for list1,list2 in zip(seq1,seq2):
        row = []
        j = 0
        for x,y in zip(list1,list2):
            mapping.update({(i,j):(x,y)})
            row.append((x, y))
            j = j+1
        i = i+1
    return mapping

# get indices of all central A's
def coordinate_finder(pattern, config):
    A_coord = []
    for i in range(len(config)):
        text = config[i]
        for j in pattern.finditer(text):
            A_coord = A_coord + [(i, j.span()[0] + 1)]
    return A_coord


pattern_MAS = re.compile('MAS')
pattern_SAM = re.compile('SAM')
lrd_diag_text = sequence_generator(b_sequence_expanded,d_sequence_expanded)
lrd_diag_coord = coord_mapper(b_sequence_expanded,d_sequence_expanded)
lrd_diag_MAS_As = coordinate_finder(pattern_MAS, lrd_diag_text)
lrd_diag_MAS_As_es = [lrd_diag_coord[x] for x in lrd_diag_MAS_As] # go back to euclidean space from lrd diagonal space

rlu_diag_text = sequence_generator(c_sequence_expanded,a_sequence_expanded)
rlu_diag_coord = coord_mapper(c_sequence_expanded,a_sequence_expanded)
rlu_diag_MAS_As = coordinate_finder(pattern_MAS, rlu_diag_text)
rlu_diag_MAS_As_es = [rlu_diag_coord[x] for x in rlu_diag_MAS_As] # go back to euclidean space from rlu diagonal space

rld_diag_text = sequence_generator(b_sequence_expanded,a_sequence_expanded)
rld_diag_coord = coord_mapper(b_sequence_expanded,a_sequence_expanded)
rld_diag_MAS_As = coordinate_finder(pattern_MAS, rld_diag_text)
rld_diag_MAS_As_es = [rld_diag_coord[x] for x in rld_diag_MAS_As] # go back to euclidean space from rld diagonal space

lru_diag_text = sequence_generator(c_sequence_expanded,d_sequence_expanded)
lru_diag_coord = coord_mapper(c_sequence_expanded,d_sequence_expanded)
lru_diag_MAS_As = coordinate_finder(pattern_MAS, lru_diag_text)
lru_diag_MAS_As_es = [lru_diag_coord[x] for x in lru_diag_MAS_As] # go back to euclidean space from lru diagonal space

all_configurations = list((lrd_diag_MAS_As_es, lru_diag_MAS_As_es, 
                          rld_diag_MAS_As_es, rlu_diag_MAS_As_es))


# find intersections of any combo of the above 4 As_es vectors
all_index_combinations = [[i,j] for i in range(len(all_configurations)) for j in range(len(all_configurations)) if i < j]
all_relevant_configurations = [[all_configurations[i], all_configurations[j]] for i,j in all_index_combinations]        
answer_collection = []
n = 0
for x,y in all_relevant_configurations:
    n = n + 1
    for i in x:
        for j in y:
            if i == j:
                answer_collection.append((i))

answer = len(set(answer_collection))
print(answer)
