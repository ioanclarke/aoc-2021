use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let nums: Vec<i32> = inp
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let mut count = 0;

    for i in 0..nums.len() - 3 {        
        if nums[i + 3] > nums[i] {
            count += 1;
        }
    }

    println!("{}", count);
    Ok(())
}