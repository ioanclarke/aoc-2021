def main():
    lines = open('in').read().split()
    illegal_characters = get_illegal_characters(lines)
    score = get_score(illegal_characters)
    print(score)    

def get_illegal_characters(lines):
    illegal_characters = []
    for line in lines:
        if (illegal_character := find_illegal_character(line)) is not None:
            illegal_characters.append(illegal_character)

    return illegal_characters



def find_illegal_character(line):
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
            return c
            
    return None


def get_score(chars):
    char_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return sum(char_scores[c] for c in chars)


main()