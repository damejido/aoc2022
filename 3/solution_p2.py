
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(letter):
  return letters.index(letter)+1

def get_largest_sack(e1, e2, e3):
  e1_size = len(e1)
  e2_size = len(e2)
  e3_size = len(e3)

  if (e1_size > e2_size and e1_size > e3_size):
    return e1
  elif (e2_size > e1_size and e2_size > e3_size):
    return e2
  else:
    return e3

priority_total = 0
groups_total = 0
with open('input.txt') as rucksacks:
  e1 = rucksacks.readline().strip()
  e2 = rucksacks.readline().strip()
  e3 = rucksacks.readline().strip()

  while (e1 != ''):
    largest_sack = get_largest_sack(e1, e2, e3)

    for i in range(len(largest_sack)):
      try:
        letter = largest_sack[i]
        e1.index(letter)
        e2.index(letter)
        e3.index(letter)
        # made it here, so all three have this letter 
        priority = get_priority(letter)
        priority_total += priority
        groups_total += 1
        print(f'found matching letter {letter} for groups e1 {e1} e2 {e2} e3 {e3} with largest_sack set to {largest_sack} priority {priority} and new total {priority_total}')
        break
      except ValueError:
        continue
    
    e1 = rucksacks.readline().strip()
    e2 = rucksacks.readline().strip()
    e3 = rucksacks.readline().strip()

  
      
print(f'Sum of all mismatching assignments {priority_total} and group total {groups_total}')