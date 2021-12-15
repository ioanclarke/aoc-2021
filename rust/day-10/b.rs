use std::fs;
use std::error::Error;
use std::collections::HashMap;


fn main() -> Result<(), Box<dyn Error>>{
    let inp = fs::read_to_string("in")?;
    let incomplete_lines: Vec<&str> = inp
        .lines()
        .filter(|line| !is_corrupt(line))
        .collect();
    let closing_sequences: Vec<Vec<char>> = incomplete_lines
        .iter()
        .map(|line| closing_sequence(line))
        .collect();
    let score: usize = get_score(closing_sequences);
    
    println!("{}", score);
    Ok(())
}


fn is_corrupt(line: &str) -> bool{
    let open_chunk_chars: Vec<char> = vec!['(', '[', '{', '<'];

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
            return true;
        }
    }
            
    false
}

fn closing_sequence(line: &str) -> Vec<char> {
    let open_chunk_chars: Vec<char> = vec!['(', '[', '{', '<'];

    let mut open_chunk_pairs = HashMap::new();
    open_chunk_pairs.insert('(', ')');
    open_chunk_pairs.insert('[', ']');
    open_chunk_pairs.insert('{', '}');
    open_chunk_pairs.insert('<', '>');

    let mut stack: Vec<char> = Vec::new();
    for c in line.chars() {
        if open_chunk_chars.contains(&c) {
            stack.push(c);
        } else {
            stack.pop();
        }
    }
    
    stack
        .iter()
        .rev()
        .map(|c| open_chunk_pairs[c])
        .collect()
}


fn get_score(sequences: Vec<Vec<char>>) -> usize {
    let mut scores: Vec<usize> = sequences
        .iter()
        .map(|seq| get_score_for_sequence(seq))
        .collect();
    scores.sort();
    scores[(scores.len() - 1) / 2]
}

fn get_score_for_sequence(chars: &Vec<char>) -> usize {
    let mut char_scores = HashMap::new();
    char_scores.insert(')', 1);
    char_scores.insert(']', 2);
    char_scores.insert('}', 3);
    char_scores.insert('>', 4);

    let mut score = 0;
    for c in chars {
        score *= 5;
        score += char_scores[&c];
    }

    score
}