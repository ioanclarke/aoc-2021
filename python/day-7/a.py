inp = sorted(list(map(int, open('in').read().split(','))))
median = (inp[len(inp) // 2 - 1] + inp[len(inp) // 2]) // 2
print(sum(abs(n - median) for n in inp))
