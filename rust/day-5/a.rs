use std::fs;
use std::error::Error;
use std::cmp::{ max, min };

struct Line {
    start: Point,
    end: Point
}

impl Line {
    fn horizontal(&self) -> bool {
        self.start.y == self.end.y
    }

    fn vertical(&self) -> bool {
        self.start.x == self.end.x
    }
}

struct Point {
    x: usize,
    y: usize
}

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("in")?;

    let lines: Vec<Line> = create_lines(inp.lines().collect());
    let vent_map: Vec<Vec<usize>> = create_vent_map(lines);
    let num_of_dangerous_areas = count_overlapping_lines(vent_map);
    println!("{}", num_of_dangerous_areas);
    
    Ok(())   
}

fn create_lines(inp: Vec<&str>) -> Vec<Line> {
    let mut lines: Vec<Line> = Vec::new();
    for line in inp {
        let pairs: Vec<&str> = line.split(" -> ").collect();
        let first_pair: &str = pairs[0];
        let second_pair: &str = pairs[1];

        let start: Point = build_point(first_pair);
        let end: Point = build_point(second_pair);

        lines.push(Line{start, end});
    }

    lines

}


fn build_point(pair: &str) -> Point {
    let coords: Vec<&str> = pair.split(',').collect();
    let x: usize = coords[0].parse().unwrap();
    let y: usize = coords[1].parse().unwrap();

    Point{x, y}
}


fn create_vent_map(lines: Vec<Line>) -> Vec<Vec<usize>> {
    let max_x = get_max_x(&lines); 
    let max_y = get_max_y(&lines);

    let mut vent_map: Vec<Vec<usize>> = vec![vec![0; max_x + 1]; max_y + 1];

    for line in lines {
        if line.horizontal() {
            draw_horizontal_line(line, &mut vent_map)
        } else if line.vertical() {
            draw_vertical_line(line, & mut vent_map)
        }
    }
            
    vent_map
}


fn count_overlapping_lines(vent_map: Vec<Vec<usize>>) -> usize {

    let mut count: usize = 0;
    for row in vent_map {
        count += row.iter().filter(|&cell| *cell > 1).count();
    }

    count
}


fn get_max_x(lines: &Vec<Line>) -> usize {
    lines
        .iter()
        .map(|line| max(line.start.x, line.end.x))
        .max()
        .unwrap()
}
    

fn get_max_y(lines: &Vec<Line>) -> usize {
    lines
        .iter()
        .map(|line| max(line.start.y, line.end.y))
        .max()
        .unwrap()
}


fn draw_horizontal_line(line: Line, vent_map: &mut Vec<Vec<usize>>) {
    let y = line.start.y;
    let x1 = line.start.x;
    let x2 = line.end.x;

    for x in min(x1, x2)..max(x1, x2) + 1 {
        vent_map[y][x] += 1;
    }
}


fn draw_vertical_line(line: Line, vent_map: &mut Vec<Vec<usize>>) {
    let x = line.start.x;
    let y1 = line.start.y;
    let y2 = line.end.y;

    for y in min(y1, y2)..max(y1, y2) + 1 {
        vent_map[y][x] += 1;
    }
}


