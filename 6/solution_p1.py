with open('input.txt') as packets:
  transmission = packets.read().strip()
  start = 0
  while start+3 <= len(transmission):
    test = set()
    test.add(transmission[start])
    test.add(transmission[start+1])
    test.add(transmission[start+2])
    test.add(transmission[start+3])
    if len(test) > 3:
      print(f'marker {start+4} with sequence {transmission[start:start+4]}')
      break
    else:
      start+=1