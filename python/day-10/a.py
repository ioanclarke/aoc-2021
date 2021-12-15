from typing import List


def main():
    lines: List[str] = open('in').read().split()
    illegal_chars: List[str] = get_illegal_chars(lines)
    score: int = get_score(illegal_chars)
    print(score)    


def get_illegal_chars(lines: List[str]):
    return [illegal_char for line in lines if (illegal_char := find_illegal_char(line)) is not None]


def find_illegal_char(line: str):
    open_chunk_chars = ['(', '[', '{', '<']
    close_chunk_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    stack: List[str] = []
    for c in line:
        if c in open_chunk_chars:
            stack.append(c)
        elif stack.pop() != close_chunk_pairs[c]:
            return c
            
    return None


def get_score(chars: List[str]):
    char_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return sum(char_scores[c] for c in chars)


main()