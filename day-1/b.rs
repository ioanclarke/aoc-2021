use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let nums: Vec<i32> = inp
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let mut count = 0;

    for i in 0..nums.len() {
        let mut sum_lower = 0;
        let mut sum_upper = 0;
        let mut n: i32;

        sum_lower += nums[i];

        n = match nums.get(i + 1){
            Some(x) => x,
            None => break
        };

        sum_lower += n;
        sum_upper += n;

        n = match nums.get(i + 2) {
            Some(x) => x,
            None => break
        };

        sum_lower += n;
        sum_upper += n;

        n = match nums.get(i + 3) {
            Some(x) => x,
            None => break
        };

        sum_upper += n;
        
        if sum_upper > sum_lower {
            count += 1;
        }

    }

    println!("count {}", count);
    Ok(())
}