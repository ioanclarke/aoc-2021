use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("in.txt")?;

    let instructions: Vec<&str> = inp
        .lines()
        .collect();

    let mut horizontal: usize = 0;
    let mut depth: usize = 0;
    let mut aim: usize = 0;

    for inst in instructions {
        let pair: Vec<&str> = inst.split_whitespace().collect();
        let direction = pair[0];
        let quantity: usize = pair[1].parse().unwrap();

        if direction == "forward" {
            horizontal += quantity;
            depth += aim * quantity
        } else if direction == "down" {
            aim += quantity
        } else if direction == "up" {
            aim -= quantity
        }
    }

    println!("{}", horizontal * depth);
    Ok(())
}