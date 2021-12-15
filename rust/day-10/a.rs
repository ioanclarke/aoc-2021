use std::fs;
use std::error::Error;
use std::collections::HashMap;


fn main() -> Result<(), Box<dyn Error>>{
    let inp = fs::read_to_string("in")?;
    let lines: Vec<&str> = inp
        .lines()
        .collect();

    let illegal_chars: Vec<char> = get_illegal_chars(lines);
    let score: usize = get_score(illegal_chars);

    println!("{}", score);
    Ok(())
}


fn get_illegal_chars(lines: Vec<&str>) -> Vec<char> {
    lines
        .iter()
        .filter_map(|line| find_illegal_char(line))
        .collect()
}


fn find_illegal_char(line: &str) -> Option<char> {
    let open_chunk_chars = vec!['(', '[', '{', '<'];
    // For some reason this gives an error
    // let close_chunk_pairs: HashMap<_, _> = [
    //     (')', '('),
    //     (']', '['),
    //     ('}', '{'),
    //     ('>', '<')
    // ].into();
    let mut close_chunk_pairs = HashMap::new();
    close_chunk_pairs.insert(')', '(');
    close_chunk_pairs.insert(']', '[');
    close_chunk_pairs.insert('}', '{');
    close_chunk_pairs.insert('>', '<');

    let mut stack: Vec<char> = Vec::new();
    for c in line.chars() {
        if open_chunk_chars.contains(&c) {
            stack.push(c);
        } else if stack.pop().unwrap() != close_chunk_pairs[&c] {
            return Some(c);
        }
    }
            
    None
}


fn get_score(chars: Vec<char>) -> usize {
    // For some reason this also gives an eror
    // let char_scores = HashMap::from([
    //     (')', 3),
    //     (']', 57),
    //     ('}', 1197),
    //     ('>', 25137)
    // ]);

    let mut char_scores = HashMap::new();
    char_scores.insert(')', 3);
    char_scores.insert(']', 57);
    char_scores.insert('}', 1197);
    char_scores.insert('>', 25137);

    chars
        .iter()
        .map(|c| char_scores[c])
        .sum()
}