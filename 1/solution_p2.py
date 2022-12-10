elf_calories = []
current_elf_calories = 0

with open('input.txt', 'r') as inputs:
  for line in inputs:
    if (line == '\n'):
      # create a new elf entry and restart sum
      elf_calories.append(current_elf_calories)
      current_elf_calories = 0
    else:
      current_elf_calories += int(line)

sorted_elf_calories = sorted(elf_calories)
top_three_total = sorted_elf_calories[-1] + sorted_elf_calories[-2] + sorted_elf_calories[-3]
print(top_three_total)