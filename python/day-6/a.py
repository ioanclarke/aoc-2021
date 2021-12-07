fish = list(map(int, open('in').read().split(',')))

for _ in range(80):
    new_fish = 0
    for i in range(len(fish)):
        if fish[i] == 0:
            new_fish += 1
        fish[i] = fish[i] - 1 if fish[i] > 0 else 6

    fish.extend([8] * new_fish)

print(len(fish))

