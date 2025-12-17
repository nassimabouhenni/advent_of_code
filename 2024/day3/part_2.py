# Day 3 Part 2
import re 

with open("advent_of_code_2024_03.txt", "r") as file:
    text = file.read()
    
multiple_strings = re.findall("mul\(\d*\,\d*\)", text)
multiple_numbers = [((re.findall("don't\(\)|do\(\)", text.split(m)[0]) or [r"do()"])[-1], 
                    re.findall(r'(\d+)', m)) for m in multiple_strings]
multiples = [m[1] for m in multiple_numbers if m[0] == r'do()']
answer = sum([int(x)*int(y) for x,y in multiples])
print(answer)
