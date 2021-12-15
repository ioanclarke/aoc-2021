from typing import Counter


def main():
    template, reactions = open('in').read().split('\n' * 2)
    reactions = build_reaction_map(reactions)
    polymer = react(template, reactions, 10)
    print(range_of(polymer))


def build_reaction_map(inst: str) -> dict:
    return {(split := x.split(' -> '))[0]: split[1] for x in inst.splitlines()}


def react(template_str: str, reactions: dict, steps: int) -> str:
    template = list(template_str)
    for _ in range(steps):
        new = [reactions[a + b] for a, b in zip(template, template[1:])]
        template = [template.pop(0) if i % 2 == 0 else new.pop(0) for i in range(len(template) + len(new))]
    return ''.join(template)


def range_of(polymer: str) -> int:
    freqs = Counter(polymer)
    return freqs.most_common()[0][1] - freqs.most_common()[-1][1]


main()