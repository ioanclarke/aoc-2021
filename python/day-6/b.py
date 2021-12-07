from collections import Counter

fish = list(map(int, open('test').read().split(',')))

fc = Counter(fish)
fc[0], fc[7], fc[8] = 0, 0, 0

print(fc)
for _ in range(1):
    new_fish = fc[0]
    fc[0] = fc[1]
    fc[1] = fc[2]
    fc[2] = fc[3]
    fc[3] = fc[4]
    fc[4] = fc[5]
    fc[5] = fc[6]
    fc[6] = fc[7] + new_fish
    fc[7] = fc[8]
    fc[8] = new_fish

    print(fc)

print(sum(fc.values()))