# Day 3 Part 1
import re 

with open("advent_of_code_2024_03.txt", "r") as file:
    text = file.read()
    
multiple_strings = re.findall("mul\(\d*\,\d*\)", text)
multiple_numbers = [re.findall(r'(\d+)', m) for m in multiple_strings]
answer = sum([int(x)*int(y) for x,y in multiple_numbers])
print(answer)
