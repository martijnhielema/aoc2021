with open('input.txt') as f:
    instructions = f.read().split('\n')

split_instructions = [[x.split(' ')[0], int(x.split(' ')[1]) ] for x in instructions]

depth = 0
x_pos = 0

for inst in split_instructions:
    if inst[0] == 'forward':
        x_pos += inst[1]
    elif inst[0] == 'down':
        depth += inst[1]
    elif inst[0] == 'up':
        depth -= inst[1]

print(depth * x_pos)

depth = 0
x_pos = 0
aim = 0

for inst in split_instructions:
    if inst[0] == 'forward':
        x_pos += inst[1]
        depth += inst[1] * aim
    elif inst[0] == 'down':
        aim += inst[1]
    elif inst[0] == 'up':
        aim -= inst[1]

print(depth * x_pos)
