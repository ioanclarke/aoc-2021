n = list(map(int, open('input.txt').read().split()))
print(sum(n[i+3] > n[i] for i in range(len(n) - 3)))