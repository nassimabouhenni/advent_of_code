# Day 2 Part 1

with open("advent_of_code_2024_02.txt", "r") as file:
    text = file.read()
    
reports = [[int(level) for level in report.split(" ")] for report in text.split("\n")]

reports_deltas = []

for report in reports:
    delta = []
    for index in range(1,len(report)):
        delta.append(report[index] - report[index-1])
    delta.sort()
    reports_deltas.append(delta)
        
safe_report_deltas = [report_deltas for report_deltas in reports_deltas 
                     if 1 <= abs(report_deltas[0]) <= 3 and 1 <= abs(report_deltas[-1]) <= 3 
                     and abs(report_deltas[0] + report_deltas[-1]) == (abs(report_deltas[-1]) + abs(report_deltas[0]))]

answer = len(safe_report_deltas)
print(answer)
