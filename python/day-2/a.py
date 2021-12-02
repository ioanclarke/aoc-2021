def main():
    instructions = open('in.txt').read().splitlines()
    horizontal = 0
    depth = 0
    for inst in instructions:
        direction, quantity = inst.split()
        quantity = int(quantity)

        if direction == "forward":
            horizontal += quantity
        elif direction == "down" :
            depth += quantity
        elif direction == "up":
            depth -= quantity
        
    print(horizontal * depth)

main()