from math import inf

inp = list(map(int, open('in').read().split(',')))
print(min(sum((diff := abs(x - n)) * (diff + 1) // 2 for x in inp) for n in range(min(inp), max(inp) + 1)))