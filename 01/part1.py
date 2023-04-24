
with open('01/input.txt', 'r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(sum(lines))
