use std::fs;
use std::error::Error;
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn Error>> {
    let fish: Vec<usize> = fs::read_to_string("in")?
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    let fish_counts = create_fish_count_map(fish);
    let num_of_fish = simulate_breeding(fish_counts, 256);

    println!("{}", num_of_fish);
    Ok(())
}

fn create_fish_count_map(fish: Vec<usize>) -> HashMap<usize, usize> {
    let mut fc = HashMap::new();
    for i in 0..=8 {
        fc.insert(i, 0);
    }
    for n in fish {
        *fc.get_mut(&n).unwrap() += 1;
    }
    fc
}

fn simulate_breeding(mut fc: HashMap<usize, usize>, days: usize) -> usize {
    for _ in 0..days {
        let new_fish = fc[&0];
        for i in 0..=7 {
            *fc.get_mut(&i).unwrap() = fc[&(i + 1)];
        }
        *fc.get_mut(&6).unwrap() += new_fish;
        *fc.get_mut(&8).unwrap() = new_fish;
    }
    
    fc.values().sum()
}