# Day 4 Part 1 

import re

with open("advent_of_code_2024_04.txt", "r") as file:
    text = file.read()

text_split = text.split("\n")
n = len(text_split) # assume square grid
# get possible sequences
sequence = [i for i in range(n)] # assume square grid

##########################
    
# Forward/Back

# forward text
forward_text = text_split

# reverse text
backward_text = text[::-1].split("\n")

##########################

# Up/Down

# text read down
down_text = []
for i in range(n):
    row = ""
    for j in range(n):
        row = row + text_split[j][i]
    down_text.append(row)

# text read up
up_text = []
for i in range(n):
    row = ""
    for j in range(n)[::-1]:
        row = row + text_split[j][i]
    up_text.append(row)

##########################

# text read diagonal (L-R, down)

# 9,89,789,etc
a_sequence_expanded = []
for i in range(n):
    a_sequence_expanded.append(sequence[n-(i+1):n])

for i in range(n):
    a_sequence_expanded.append(sequence[0:n-(i+1)])
    
# 0,01,012,etc
b_sequence_expanded = []
for i in range(n):
    b_sequence_expanded.append(sequence[0:i+1])

for i in range(n):
    b_sequence_expanded.append(sequence[i+1:n])
    
# 9,98,987,etc
c_sequence_expanded = []
for i in range(n):
    c_sequence_expanded.append(sequence[n-(i+1):n][::-1])

for i in range(n):
    c_sequence_expanded.append(sequence[0:n-(i+1)][::-1])

# 0,10,210,etc    
d_sequence_expanded = []
for i in range(n):
    d_sequence_expanded.append(sequence[0:i+1][::-1])

for i in range(n):
    d_sequence_expanded.append(sequence[i+1:n][::-1])

# Select sequences based on diag type

lrd_diag_text = []
for list1,list2 in zip(b_sequence_expanded,d_sequence_expanded):
    row = ""
    for x,y in zip(list1,list2):
        row = row + text_split[x][y]
    lrd_diag_text.append(row)
    
rlu_diag_text = []
for list1,list2 in zip(c_sequence_expanded,a_sequence_expanded):
    row = ""
    for x,y in zip(list1,list2):
        row = row + text_split[x][y]
    rlu_diag_text.append(row)
    
rld_diag_text = []
for list1,list2 in zip(b_sequence_expanded,a_sequence_expanded):
    row = ""
    for x,y in zip(list1,list2):
        row = row + text_split[x][y]
    rld_diag_text.append(row)
    
lru_diag_text = []
for list1,list2 in zip(c_sequence_expanded,d_sequence_expanded):
    row = ""
    for x,y in zip(list1,list2):
        row = row + text_split[x][y]
    lru_diag_text.append(row)
    
all_configurations = list((forward_text, backward_text, down_text, up_text, lrd_diag_text, lru_diag_text, 
                          rld_diag_text, rlu_diag_text))

answer = sum([sum([len(re.findall('XMAS', row)) for row in config]) for config in all_configurations])
print(answer)
