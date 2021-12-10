from typing import List


def main():
    lines = open('in').read().split()
    incomplete_lines = [line for line in lines if not is_corrupt(line)]
    closing_sequences = [find_closing_sequence(line) for line in lines]
    score = get_score(closing_sequences)
    print(score)


def is_corrupt(line: str) -> bool:
    open_chunk_chars = ['(', '[', '{', '<']
    close_chunk_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    stack = []
    for c in line:
        if c in open_chunk_chars:
            stack.append(c)
        elif stack.pop() != close_chunk_pairs[c]:
            return True
            
    return False


def find_closing_sequence(line: str) -> str:
    open_chunk_chars = ['(', '[', '{', '<']
    open_chunk_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    stack = []
    for c in line:
        if c in open_chunk_chars:
            stack.append(c)
        else:
            stack.pop()
            
    return ''.join(reversed([open_chunk_pairs[c] for c in stack]))


def get_score(sequences: List[str]) -> int:
    scores = sorted([get_score_for_sequence(seq) for seq in sequences])
    return scores[(len(scores) - 1) // 2]


def get_score_for_sequence(seq: str) -> int:
    char_scores: dict[str, int] = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score: int = 0
    
    for c in seq:
        score *= 5
        score += char_scores[c]

    return score


main()