with open('input1.txt') as f:
    list = [int(x.strip()) for x in f.readlines()]

print(list[0], list[-1])

increases = 0
for i in range(0, len(list) - 1):
    if list[i] < list[i+1]:
        increases += 1

print(f'The number of times depth increases: {increases}')

increase_sliding = 0
for i in range(0, len(list) - 3):
    first_window = list[i] + list[i+1] + list[i+2]
    second_window = list[i+1] + list[i+2] + list[i+3]
    if first_window < second_window:
        increase_sliding += 1

print(f'The number of times the sliding window increases: {increase_sliding}')
