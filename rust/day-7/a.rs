use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("in")?;
    let mut nums: Vec<usize> = inp
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    nums.sort();

    // println!("{:?}", nums);

    let l: usize = nums.len();
    let median: usize = (nums[l / 2 - 1] + nums[l / 2]) / 2;
    // println!("{}", median);

    // for n in nums {
    //     println!("{}", n as isize - median as isize)
    // }
    let fuel: isize = nums
        .iter()
        .map(|n| ((*n as isize - median as isize) as isize).abs())
        .sum();

    println!("{}", fuel);

    Ok(())
}