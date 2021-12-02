instructions = [line.split() for line in open('in.txt').read().splitlines()]
d = lambda direction: sum(int(x[1]) for x in instructions if x[0] == direction)
print(d('forward') * (d('down') - d('up')))