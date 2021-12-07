use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("test")?;
    let mut fish: Vec<usize> = inp
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    for _ in 0..80{
        let mut new_fish = 0;
        for i in 0..fish.len() {
            if fish[i] == 0 {
                new_fish += 1;
            }
            fish[i] = if fish[i] > 0 { fish[i] - 1 } else { 6 };
        }
        let new: Vec<usize> = vec![8; new_fish];
        fish.extend(new);
    }

    println!("{}", fish.len());
    Ok(())
}