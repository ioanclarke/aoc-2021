n = list(map(int, open('in.txt')))
print(sum(n[i+3] > n[i] for i in range(len(n) - 3)))