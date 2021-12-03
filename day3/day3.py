import copy
from collections import defaultdict

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]


def most_common_binary(l: list[int]) -> str:
    if l.count('1') >= len(l) / 2:
        return '1'
    else:
        return '0'


def least_common_binary(l: list[int]) -> str:
    if l.count('1') < len(l) / 2:
        return '1'
    else:
        return '0'


position_dict = defaultdict(list)

for i in range(0, len(lines[0])):
    for j in lines:
        position_dict[i].append(int(j[i]))

gamma = int(''.join(list(map(most_common_binary, position_dict.values()))), 2)
epsilon = int(''.join(list(map(least_common_binary, position_dict.values()))), 2)
print(f'The result of part one is: {gamma * epsilon}')


def filter_by_function_position(func, list_of_codes, position):
    position_values = []
    for i in list_of_codes:
        position_values.append(i[position])

    filter_val = func(position_values)
    new_list = [x for x in list_of_codes if x[position] == filter_val]

    return new_list

filtered_list = copy.deepcopy(lines)
i = 0
while len(filtered_list) > 1:
    filtered_list = filter_by_function_position(most_common_binary, filtered_list, i)
    i += 1

oxygen = int(filtered_list[0], 2)

filtered_list = copy.deepcopy(lines)
i = 0
while len(filtered_list) > 1:
    filtered_list = filter_by_function_position(least_common_binary, filtered_list, i)
    i += 1

co2 = int(filtered_list[0], 2)

print(f'The result of part 2 is: {oxygen * co2}')
