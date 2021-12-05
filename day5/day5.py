import numpy as np

with open('input.txt') as f:
    lines = f.read().split('\n')

coordinates = []
for x in lines:
    splits = [list(map(int, y.split(','))) for y in x.split(' -> ')]
    # line = {'x1': splits[0][0], 'y1': splits[0][1], 'x2': splits[1][0], 'y2': splits[1][1]}
    coordinates.append(splits)

max_x = 0
max_y = 0

for i in coordinates:
    if i[0][0] > max_x:
        max_x = i[0][0]
    if i[1][0] > max_x:
        max_x = i[1][0]

    if i[0][1] > max_y:
        max_y = i[0][1]
    if i[1][1] > max_x:
        max_y = i[1][1]

print(max_x, max_y)
thermals = np.zeros((max_x + 2, max_y + 2))
print(np.shape(thermals))
for i in coordinates:
    x1 = i[0][0]
    y1 = i[0][1]
    x2 = i[1][0]
    y2 = i[1][1]

    if y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            thermals[j][y1] += 1
    elif x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            thermals[x1][j] += 1

print(np.count_nonzero(thermals >= 2))
