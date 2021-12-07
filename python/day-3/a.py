inp = open('in').read().split()
# gamma = int(''.join([max(bits:=[x[i] for x in inp], key=bits.count) for i in range(len(inp[0]))]), 2)
# epsilon = gamma ^ (2 ** (len(str(gamma)) + 1) - 1)

most_common = [max(bits:=[x[i] for x in inp], key=bits.count) for i in range(len(inp[0]))]
least_common = ['1' if x == '0' else '0' for x in most_common]
gamma = int(''.join(most_common), 2)
epsilon = int(''.join(least_common), 2)
print(f'{gamma=}')
print(f'{epsilon=}')
print(gamma * epsilon)
