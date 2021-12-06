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


def horizontal_line(from_coordinate, to_coordinate):
    line = []
    for i in range(from_coordinate[0], to_coordinate[0] + 1):
        line.append((i, from_coordinate[1]))

    return line


def vertical_line(from_coordinate, to_coordinate):
    line = []
    for i in range(from_coordinate[1], to_coordinate[1] + 1):
        line.append((from_coordinate[0], i))

    return line


thermals = np.zeros((max_x + 2, max_y + 2))
for i in coordinates:
    from_coordinate = i[0]
    to_coordinate = i[1]
    from_x = from_coordinate[0]
    from_y = from_coordinate[1]
    to_x = to_coordinate[0]
    to_y = to_coordinate[1]

    if from_y == to_y:
        line_coordinates = horizontal_line(from_coordinate, to_coordinate)
    elif from_x == to_x:
        line_coordinates = vertical_line(from_coordinate, to_coordinate)

    for coordinate in line_coordinates:
        thermals[coordinate[0]][coordinate[1]] += 1


print(np.count_nonzero(thermals >= 2))
