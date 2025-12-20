# Import from base python
import re
import math

# Define starting position for dial
x_i = 50

# Import rotations
# rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
with open("./advent_of_code_2025_01.txt", "r") as file:
    rotations = file.readlines()
    
rotations = [rotation.strip('\n') for rotation in rotations]

# Sanitize rotations
rotations = [int(re.sub('R', '', re.sub('L', '-', rotation))) for rotation in rotations]

dial_positions = [x_i]
num_zeros = 0
for index, rotation in enumerate(rotations):
    dial_positions.append((dial_positions[index]+rotation)%100)
    total_rotations = math.floor(abs(rotation)/100)
    net_rotation = math.copysign(abs(rotation)%100, rotation)
    
    if dial_positions[index] == 0:
        hits_zero = 0
    elif (dial_positions[index] + net_rotation)%100 == 0:
        hits_zero = 1
    elif rotation > 0 and (dial_positions[index] + net_rotation)%100 < dial_positions[index]:
        hits_zero = 1
    elif rotation < 0 and (dial_positions[index] + net_rotation)%100 > dial_positions[index]:
        hits_zero = 1
    else:
        hits_zero = 0
        
    num_zeros = num_zeros + hits_zero + total_rotations 
    
answer_p1 = len([dial_position for dial_position in dial_positions if dial_position == 0])

answer_p2 = num_zeros

print(answer_p1)

print(answer_p2) 
