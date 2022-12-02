# Part 1

# with open("../inputs/day01.csv") as f:

#     total = 0
#     highest = 0

#     for line in f:
#         if line == '\n':
#             if total > highest:
#                 highest = total

#             # Reseting total value after each linebreak
#             total = 0
#         else:
#             total += int(line)

# print("@@@@@@ OUTPUT @@@@@@")
# print(highest)

# Part 2

with open("../inputs/day01.csv") as f:

    calories = []
    total = 0

    for line in f:
        if line == '\n':
            calories.append(total)

            # Reseting total value after each linebreak
            total = 0
        else:
            total += int(line)


calories.sort(reverse=True)

print("@@@@@@ OUTPUT @@@@@@")
print(calories[0] + calories[1] + calories[2])