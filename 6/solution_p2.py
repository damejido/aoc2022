with open('input.txt') as packets:
  transmission = packets.read().strip()
  start = 0
  while start+3 <= len(transmission):
    test = set()
    for i in range(start, start+14):
      test.add(transmission[i])
    if len(test) > 13:
      print(f'marker {start+14} with sequence {transmission[start:start+14]}')
      break
    else:
      start+=1