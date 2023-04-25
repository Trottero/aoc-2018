
with open('02/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def compute_distance(word1, word2):
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance


for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if compute_distance(lines[i], lines[j]) == 1:
            print(lines[i])
            print(lines[j])

            # Find the offending character remove it and print
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    print(lines[i][:k] + lines[i][k + 1:])
                    break
