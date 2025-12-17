# Day 1 Part 2

with open("advent_of_code_2024_01.txt", "r") as file:
    text = file.read()

text = text.split("\n")

list1 = [int(t.split("   ")[0]) for t in text]
list2 = [(t.split("   ")[1]) for t in text]

unique_list = list(set(list2))

location_id_dict_precursor = [[int(b),len(list(filter(lambda a: a == b, list2)))] for b in unique_list]
location_id_dict_0 = [x[0] for x in location_id_dict_precursor]
location_id_dict_1 = [x[1] for x in location_id_dict_precursor]
location_id_dict = dict(zip(location_id_dict_0, location_id_dict_1))

answer = 0
for i in list1:
    try:
        location_id_dict[i]
        answer = answer + i*location_id_dict[i]
    except:
        answer = answer + 0
        
print(answer)
