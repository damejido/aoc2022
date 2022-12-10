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

print(sorted(elf_calories)[-1])