def main():
    inp = open('in').read().split()
    gamma = get_num(inp.copy(), '1', max)
    epsilon = get_num(inp.copy(), '0', min)
    print(gamma * epsilon)

def get_num(inp, default, counter):
    i = 0
    while len(inp) > 1:
        bits = [x[i] for x in inp]
        common = default if bits.count('1') == bits.count('0') else counter(bits, key=bits.count)
        inp = [x for x in inp if x[i] == common]
        i += 1
    
    return int(''.join(inp[0]), 2)

main()