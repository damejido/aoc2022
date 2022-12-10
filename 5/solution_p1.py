class Crate:
  value = None

  def __repr__(self) -> str:
    return self.value if type(self.value) is str else '    '

  def __str__(self) -> str:
    return self.value if type(self.value) is str else '    '

  def __init__(self, value=None) -> None:
    self.value = value

def print_stacks(stacks: dict):
  print()
  largest_line = 0
  for value in stacks.values():
    current_len = len(value)
    largest_line = current_len if current_len > largest_line else largest_line
  
  for i in range(largest_line, 0, -1):
    for key in stacks.keys():
      if (len(stacks[key]) >= i):
        print(stacks[key][i-1], end=' ')
      else:
        print('    ', end='')
    print()
  for i in range(1, 10):
    print(f' {i}  ', end='')


if __name__ == "__main__":
  # read input of initial configuration
  stacks = {}
  for i in range(9):
    stacks[i] = []

  with open('initial_configuration.txt') as initial_config:
    for line in initial_config:
      for i in range(9):
        crate_raw = line[i*4:i*4+4].strip()
        if len(crate_raw) > 1 and crate_raw != '':
          stacks[i].append(Crate(crate_raw))
  
  for key in stacks.keys():
    stacks[key].reverse()
  
  digits_re = re.compile('\d{*}')
  with open('crate_movements.txt') as movements:
    for line in movements:
      movement_parts = line.split(' ')
      (count, source, target) = (int(movement_parts[1]), int(movement_parts[3])-1, int(movement_parts[5])-1)
      for i in range(count):
        if (len(stacks[source]) > 0):
          crate = stacks[source].pop()
          stacks[target].append(crate)
        else: 
          break

  for key in stacks.keys():
    print(stacks[key].pop())


