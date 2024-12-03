reports = list()

with open("input.txt", "r") as reports_file:
    for report in reports_file:
        levels = report.split(" ")
        levels[-1] = levels[-1].strip("\n")
        levels = [int(i) for i in levels]
        reports.append(levels)

def check_levels(report: list) -> bool:
    ascending = sorted(report)
    descending = sorted(report, reverse=True)
    if report == ascending:
        increase = True
    elif report == descending:
        increase = False
    else:
        return False

    for i in range(len(report)):
        if i == len(report) - 1:
            break
        if abs(report[i] - report[i + 1]) > 3:
            return False
        if report[i] == report[i + 1]:
            return False
        if increase and report[i] > report[i + 1]:
            return False
        if not increase and report[i] < report[i + 1]:
            return False

    return True

def levels_dampener(report: list) -> bool:
    results = list()
    for i in range(len(report)):
        temp = report.copy()
        del temp[i]
        results.append(check_levels(temp))

    for val in results:
        if val:
            return True

    return False

# Part 1
is_unsafe = 0
for report in reports:
    if not check_levels(report):
        is_unsafe += 1

print(f"Safe reports: {len(reports) - is_unsafe}")

# Part 2
is_unsafe_dampened = 0
for report in reports:
    if not levels_dampener(report):
        is_unsafe_dampened += 1

print(f"Safe reports (dampened): {len(reports) - is_unsafe_dampened}")