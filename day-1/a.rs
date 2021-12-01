use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let nums: Vec<i32> = inp
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let mut count = 0;

    for i in 1..nums.len() {
        if nums[i] > nums[i - 1] {
            count += 1;
        }
    }

    println!("{}", count);
    Ok(())

    
}