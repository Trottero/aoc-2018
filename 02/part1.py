
with open('02/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

occ_2 = 0
occ_3 = 0

for l in lines:
    letter_counts = {}
    for letter in l:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    if 2 in letter_counts.values():
        occ_2 += 1
    if 3 in letter_counts.values():
        occ_3 += 1

print(occ_2 * occ_3)
