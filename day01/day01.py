
with open("../inputs/day01.csv") as f:

    total = 0
    highest = 0

    for line in f:
        if line == '\n':
            if total > highest:
                highest = total

            # Reseting total value after each linebreak
            total = 0
        else:
            total += int(line)

print("@@@@@@ OUTPUT @@@@@@")
print(highest)
