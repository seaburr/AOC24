with open("input.txt", "r") as file:
    map = list()
    for line in file.read().splitlines():
        map.append(line)

y_max, x_max = len(map[0]), len(map)
dirs = [(1,0),
        (1,1),
        (0,1),
        (-1,1),
        (-1,0),
        (-1,-1),
        (0,-1),
        (1,-1),
        ]

def valid(position):
    return 0 <= position[0] < y_max and 0 <= position[1] < x_max

def next(position, direction):
    return position[0] + direction[0], position[1] + direction[1]

def is_there_an_xmas(position, direction):
    j, i = position
    r = 0
    while r < 4 and valid((j,i)) and map[j][i] == 'XMAS'[r]:
        j, i = next((j,i), direction)
        r += 1
    return r == 4

part_1 = 0
for x in range(x_max):
    for y in range(y_max):
        pos = y, x
        for dir in dirs:
            if is_there_an_xmas(pos, dir):
                part_1 += 1
print('Part 1:', part_1)

def prev(position, direction):
    return position[0] - direction[0], position[1] - direction[1]

def is_there_a_mas(position, direction):
    j, i = position
    j_prev, i_prev = prev(position, direction)
    j_next, i_next = next(position, direction)
    return (valid((j_prev, i_prev)) and
            valid((j_next, i_next)) and
            map[j][i] == 'A' and
            (map[j_prev][i_prev] == 'M' and
             map[j_next][i_next] == 'S' or
             map[j_prev][i_prev] == 'S' and
             map[j_next][i_next] == 'M')
            )

part_2 = 0
for x in range(x_max):
    for y in range(y_max):
        pos = y, x
        if is_there_a_mas(pos, (1,1)) and is_there_a_mas(pos, (1,-1)):
            part_2 += 1

print('Part 2:', part_2)