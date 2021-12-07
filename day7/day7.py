with open('input.txt') as f:
    positions = [int(x) for x in f.read().strip().split(',')]\

min_fuel = 0
for i in range(min(positions), max(positions)):
    fuel_spent = sum([abs(a - i) for a in positions])
    if min_fuel == 0:
        min_fuel = fuel_spent
    else:
        min_fuel = min(min_fuel, fuel_spent)

print(f'Part one: {min_fuel}')

# precalc all fuel spendings
spends = {i: sum(range(1, i + 1)) for i in range(0, max(positions) + 1)}

min_fuel = 0
for i in range(min(positions), max(positions)):
    fuel_spent = sum([spends[abs(a - i)] for a in positions])
    if min_fuel == 0:
        min_fuel = fuel_spent
    else:
        min_fuel = min(min_fuel, fuel_spent)

print(f'Part two: {min_fuel}')
