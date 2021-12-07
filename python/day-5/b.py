def main():
    inp = open('in')
    lines = create_lines(inp)
    vent_map = create_vent_map(lines)
    num_of_dangerous_areas = count_overlapping_lines(vent_map)
    print(num_of_dangerous_areas)


def create_lines(inp):
    lines = []
    for line in inp:
        first_pair, second_pair = line.split(' -> ')
        x1, y1 = first_pair.split(',')
        x2, y2 = second_pair.split(',')
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
            
    return lines
    

def create_vent_map(lines):
    max_y = get_max_y(lines)
    max_x = get_max_x(lines)

    vent_map = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for line in lines:
        if horizontal(line):
            draw_horizontal_line(line, vent_map)
        elif vertical(line):
            draw_vertical_line(line, vent_map)
        else:
            draw_diagonal_line(line, vent_map)
            
    return vent_map


def count_overlapping_lines(vent_map):
    return sum(cell > 1 for row in vent_map for cell in row)


def get_max_x(lines):
    return max(max(line[0][0], line[1][0]) for line in lines)


def get_max_y(lines):
    return max(max(line[0][1], line[1][1]) for line in lines)


def horizontal(line):
    return line[0][1] == line[1][1]


def vertical(line):
    return line[0][0] == line[1][0]


def draw_horizontal_line(line, vent_map):
    y = line[0][1]
    x1 = line[0][0]
    x2 = line[1][0]

    for x in range(min(x1, x2), max(x1, x2) + 1):
        vent_map[y][x] += 1


def draw_vertical_line(line, vent_map):
    x = line[0][0]
    y1 = line[0][1]
    y2 = line[1][1]

    for y in range(min(y1, y2), max(y1, y2) + 1):
        vent_map[y][x] += 1


def draw_diagonal_line(line, vent_map):
    x1, x2 = line[0][0], line[1][0]
    y1, y2 = line[0][1], line[1][1]

    x_step = 1 if x1 < x2 else -1
    x2 = x2 + 1 if x1 < x2 else x2 - 1

    y_step = 1 if y1 < y2 else -1
    y2 = y2 + 1 if y1 < y2  else y2 - 1

    for x, y in zip(range(x1, x2, x_step), range(y1, y2, y_step)):
        vent_map[y][x] += 1


main()