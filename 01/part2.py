
with open('01/input.txt', 'r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

freqs = []

current_freq = 0
index = 0
while True:
    current_freq += lines[index % len(lines)]
    if current_freq in freqs:
        print(current_freq)
        break
    freqs.append(current_freq)
    index += 1
