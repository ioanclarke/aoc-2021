use std::fs;
use std::error::Error;
use std::cmp::{max_by_key, min_by_key};
use std::iter::FromIterator;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("test")?;
    let bins: Vec<&str> = inp
        .lines()
        .map(|line| line.trim())
        .collect();

    let gamma = get_num(bins, '1', max_by_key);
    let epsilon = get_num(bins, '0', min_by_key);

    println!("{}", gamma * epsilon);
    Ok(())
}

fn get_num(bins: Vec<&str>, default: char, counter: fn(<T, F, K>(v1: T, v2: T, f: F) -> T ) -> usize{
    let mut i = 0;
    let mut common: char;
    while bins.len() > 1 {
        let bits: Vec<char> = bins
                .iter()
                .map(|b| b.chars().nth(i).unwrap())
                .collect();
        let frequency = |a: &char| bits.iter().filter(|&x| x == a).count();

        common = if frequency(&'1') == frequency(&'0') {default} else {counter('1', '0', frequency)};
        bins = bins
            .iter()
            .filter(|x| x.chars().nth(i).unwrap() == common)
            .collect();
        i += 1;
    }
    
    usize::from_str_radix(&String::from_iter(bins[0]), 2).unwrap()
}