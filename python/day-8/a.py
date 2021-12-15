output_values = [line[line.find('|') + 2:].strip().split() for line in open('in')]
values = [x for vals in output_values for x in vals]
print(sum(len(x) in {2, 3, 4, 7} for x in values))