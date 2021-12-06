from collections import defaultdict

with open('input.txt') as f:
    lanternfish = [int(x) for x in f.read().strip().split(',')]
    lanternfish_fast = lanternfish.copy()


CYCLES = 80
FAST_CYCLES = 256


def cycle_naive(fishlist):
    for i in range(0, len(fishlist)):
        days = fishlist[i]
        if days == 0:
            fishlist[i] = 6
            fishlist.append(8)
        else:
            fishlist[i] -= 1

    return fishlist


def make_fishdict(fishlist):
    fishdict = {}
    for i in range(0, 9):
        fishdict[i] = fishlist.count(i)
        print(f'{i}: {fishlist.count(i)}')
    return fishdict


def cycle_fast(fishdict):
    new_dict = defaultdict(int)
    for i in range(0,9):
        if i == 0:
            new_fish = fishdict[0]
        else:
            new_dict[i-1] = fishdict[i]

    new_dict[6] += new_fish
    new_dict[8] = new_fish

    return new_dict


# print(f'Initial: {[x["days"] for x in lanternfish]}')

for i in range(0, CYCLES):
    cycle_naive(lanternfish)
    # print(f'Day {i+1}: {[x["days"] for x in lanternfish]}')

fishdict = make_fishdict(lanternfish_fast)

for i in range(0, FAST_CYCLES):
    fishdict = cycle_fast(fishdict)

fish = 0
for i in fishdict.keys():
    fish += fishdict[i]

print(f'Number of fish after {CYCLES} days: {len(lanternfish)}')
print(f'Number of fish after {FAST_CYCLES} days: {fish}')

