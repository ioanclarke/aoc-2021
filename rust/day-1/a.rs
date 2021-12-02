use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let nums: Vec<usize> = fs::read_to_string("in.txt")?
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let count = (1..nums.len())
        .filter(|i| nums[*i] > nums[*i - 1])
        .count();

    println!("{}", count);
    Ok(())

    
}