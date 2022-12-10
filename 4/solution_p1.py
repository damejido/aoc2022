
#return true if a completely covers b
def covers(a, b):
  return b[0] >= a[0] and b[0] <= a[1] \
    and b[1] >= a[0] and b[1] <= a[1]

total_covers = 0

with open('input.txt') as pairs:
  for line in pairs:
    (astr, bstr) = line.strip().split(',')
    astr = astr.split('-')
    a = [int(astr[0]), int(astr[1])]
    a.sort()

    bstr = bstr.split('-')
    b = [int(bstr[0]), int(bstr[1])]
    b.sort()

    print(f'a {a} b {b}')
    if (covers(a,b) or covers(b,a)):
      print('covers!')
      total_covers +=1

print(total_covers)