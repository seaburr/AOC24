total_distance = 0
similarity_score = 0
column_a = list()
column_b = list()

with open("input.txt", "r") as input:
    for row in input:
        column_a.append(int(row.split("   ")[0]))
        column_b.append(int(row.split("   ")[-1]))

column_a = sorted(column_a)
column_b = sorted(column_b)

for i in range (len(column_a)):
    value = column_a[i] - column_b[i]
    total_distance += abs(value)

print(f"Total Distance: {total_distance}")

for i in range (len(column_a)):
    count = column_b.count(column_a[i])
    similarity_score += count * column_a[i]

print(f"Similarity Score: {similarity_score}")
