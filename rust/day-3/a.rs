use std::fs;
use std::error::Error;
use std::cmp::{max_by_key};
use std::iter::FromIterator;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("in")?;
    let bins: Vec<&str> = inp
        .lines()
        .map(|line| line.trim())
        .collect();

    let mut bits: Vec<char>;
    let mut most_common_bits: Vec<char> = Vec::new();
    
    for i in 0..bins[0].len() {
        bits = bins
            .iter()
            .map(|b| b.chars().nth(i).unwrap())
            .collect();        
            
        most_common_bits.push(max_by_key('1', '0', frequency));
    }

    let least_common_bits: Vec<char> = most_common_bits
        .iter()
        .map(|b| if *b == '1' {'0'} else {'1'})
        .collect();

    let gamma = usize::from_str_radix(&String::from_iter(most_common_bits), 2).unwrap();
    let epsilon = usize::from_str_radix(&String::from_iter(least_common_bits), 2).unwrap();
    println!("{}", gamma * epsilon);
    Ok(())
}