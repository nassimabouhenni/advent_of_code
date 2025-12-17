# Day 5 Part 1

# data cleaning
with open("advent_of_code_2024_05.txt", "r") as file:
    text = file.read()

orders = text.split("\n\n")[0].split("\n")
updates = text.split("\n\n")[1].split("\n")   
    
list1 = [int(t.split("|")[0]) for t in orders]
list2 = [int(t.split("|")[1]) for t in orders]

orders = [(i,j) for i,j in zip(list1, list2)]
updates = [[int(j) for j in i.split(",")] for i in updates]

# updates already in the right order

