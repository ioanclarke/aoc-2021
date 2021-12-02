instructions = [line.split() for line in open('in.txt').read().splitlines()]
distance_travelled = lambda direction: sum(int(x[1]) for x in instructions if x[0] == direction)
print(distance_travelled('forward') * (distance_travelled('down') - distance_travelled('up')))