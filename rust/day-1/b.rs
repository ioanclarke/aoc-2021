use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let nums: Vec<usize> = fs::read_to_string("in.txt")?
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let count = (0..nums.len() - 3)
        .filter(|i| nums[i + 3] > nums[*i])
        .count();

    println!("{}", count);
    Ok(())
}