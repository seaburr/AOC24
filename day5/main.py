sum_pt_1 = 0
sum_pt_2 = 0
page_order_rules = list()
page_collection = list()

with open("input.txt") as file:
    for line in file.readlines():
        if "|" in line:
            line = line.rstrip().split("|")
            page_order_rules.append(line[0] + line[1])
        elif "," in line:
            page_collection.append(line.strip("\n"))

def is_sorted(data: list) -> bool:
    if all(data[i] + data[i + 1] in page_order_rules for i in range(len(data) - 1)):
        return True
    return False

for update in page_collection:
    update = update.split(',')
    middle_index = (len(update) - 1) // 2
    sorted = is_sorted(update)

    if sorted:
        sum_pt_1 += int(update[middle_index])
        continue

    while not sorted:
        for i in range(len(update) - 1):
            if update[i] + update[i + 1] not in page_order_rules:
                update[i], update[i + 1] = update[i + 1], update[i]
        sorted = is_sorted(update)

    sum_pt_2 += int(update[middle_index])

print(f"Part 1: {sum_pt_1}")
print(f"Part 2: {sum_pt_2}")