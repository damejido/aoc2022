
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(letter):
  return letters.index(letter)+1

priority_total = 0
line_total = 0
with open('input.txt') as rucksacks:
  for line in rucksacks:
    line = line.strip()
    line_length = len(line)
    half_length = line_length//2
    lh = line[0:half_length]
    rh = line[half_length:line_length]
    conflict = None
    for i in range(half_length):
      try:
        rh.index(lh[i])
        conflict = lh[i]
        priority = letters.index(conflict)+1
        priority_total += priority
        line_total+=1
        print(f'Found conflict {conflict} in string {line} with lh {lh} and rh {rh} and added priority {priority} to total {priority_total}')
        break
      except ValueError:
        continue
    
print(f'Sum of all mismatching assignments {priority_total} and line total {line_total}')