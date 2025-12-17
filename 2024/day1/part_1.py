# Day 1 Part 1

with open("advent_of_code_2024_01.txt", "r") as file:
    text = file.read()

text = text.split("\n")

list1 = [int(t.split("   ")[0]) for t in text]
list1.sort()
list2 = [int(t.split("   ")[1]) for t in text]
list2.sort()

diff = 0
for i in range(len(list1)):
    diff = diff + abs(list2[i] - list1[i])
    
print(diff)
