def main():
    instructions = open('in.txt')
    horizontal = 0
    depth = 0
    aim = 0

    for inst in instructions:
        direction, quantity = inst.split()
        quantity = int(quantity)

        if direction == "forward":
            horizontal += quantity
            depth += aim * quantity
        elif direction == "down" :
            aim += quantity
        elif direction == "up":
            aim -= quantity
        
    print(horizontal * depth)

main()