# Day 2 Part 2

with open("advent_of_code_2024_02.txt", "r") as file:
    text = file.read()
    
reports = [[int(level) for level in report.split(" ")] for report in text.split("\n")]

reports_diff = []

for r in reports:
    report_combinations = [[r[j] for j in set(range(len(r)))-{i}] for i in range(len(r))]
    report_combinations.append(r)
    report_diff = []
    for report in report_combinations:
        diff = []
        for index in range(1,len(report)):
            diff.append(report[index] - report[index-1])
        diff.sort()
        report_diff.append(diff)
    reports_diff.append(report_diff)
    
safe_report_combination_diffs = [[r for r in report_diff if 1 <= abs(r[0]) <= 3 and 1 <= abs(r[-1]) <= 3 
                     and abs(r[0] + r[-1]) == (abs(r[-1]) + abs(r[0]))] for report_diff in reports_diff 
                     ]
safe_report_diffs = [r for r in safe_report_combination_diffs if r]

answer = len(safe_report_diffs)
print(answer)
