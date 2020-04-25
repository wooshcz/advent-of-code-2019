import math

inputfield = [
'#.#....#.#......#.....#......####.',
'#....#....##...#..#..##....#.##..#',
'#.#..#....#..#....##...###......##',
'...........##..##..##.####.#......',
'...##..##....##.#.....#.##....#..#',
'..##.....#..#.......#.#.........##',
'...###..##.###.#..................',
'.##...###.#.#.......#.#...##..#.#.',
'...#...##....#....##.#.....#...#.#',
'..##........#.#...#..#...##...##..',
'..#.##.......#..#......#.....##..#',
'....###..#..#...###...#.###...#.##',
'..#........#....#.....##.....#.#.#',
'...#....#.....#..#...###........#.',
'.##...#........#.#...#...##.......',
'.#....#.#.#.#.....#...........#...',
'.......###.##...#..#.#....#..##..#',
'#..#..###.#.......##....##.#..#...',
'..##...#.#.#........##..#..#.#..#.',
'.#.##..#.......#.#.#.........##.##',
'...#.#.....#.#....###.#.........#.',
'.#..#.##...#......#......#..##....',
'.##....#.#......##...#....#.##..#.',
'#..#..#..#...........#......##...#',
'#....##...#......#.###.#..#.#...#.',
'#......#.#.#.#....###..##.##...##.',
'......#.......#.#.#.#...#...##....',
'....##..#.....#.......#....#...#..',
'.#........#....#...#.#..#....#....',
'.#.##.##..##.#.#####..........##..',
'..####...##.#.....##.............#',
'....##......#.#..#....###....##...',
'......#..#.#####.#................',
'.#....#.#..#.###....##.......##.#.'
]

def cleanLoS(pivot, candidate):
  #print("Pivot: "+str(pivot[0])+", "+str(pivot[1]))
  #print("Candidate: "+str(candidate[0])+", "+str(candidate[1]))
  for i in range(1, gcd):
    checkx = int(pivot[0] + (candidate[0] - pivot[0])/gcd*i)
    checky = int(pivot[1] + (candidate[1] - pivot[1])/gcd*i)
    check = asteroids.get((checkx, checky))
    #print("Checking: "+str(checkx)+", "+str(checky)+". Result: "+str(check))
    if check != None:
      return False
  return True

def map(field):
  x = y = i = 0
  asteroids = {}
  for line in field:
    x = 0
    for char in line:
      if char == '#':
        #print("Asteroid - X:"+str(x)+"; Y:"+str(y)+".")
        asteroids[(x,y)] = 0
        #asteroids.append({'ind': i,'x': x, 'y': y, 'sees': 0})
        i += 1
      x += 1
    y += 1
  return asteroids

asteroids = map(inputfield)
print("Asteroid count: "+str(len(asteroids)))

#[(32,33)]:
for pivot in asteroids.keys():
  #print("Pivot: "+str(pivot[0])+", "+str(pivot[1]))
  for candidate in asteroids.keys():
    distx = abs(pivot[0] - candidate[0])
    disty = abs(pivot[1] - candidate[1])
    gcd = math.gcd(distx, disty)
    #print(gcd)
    if gcd-1 > 0:
      if cleanLoS(pivot, candidate) == True:
        asteroids[pivot] += 1
    elif gcd-1 == 0:
      asteroids[pivot] += 1

a_sorted = sorted(asteroids.items(), key=lambda x: x[1], reverse=True)
print("Best position: "+str(a_sorted[0]))

# (20,20) is the best position
angles = {}
for pivot in [(20,20)]:
  for candidate in asteroids.keys():
    print("Candidate: "+str(candidate[0])+", "+str(candidate[1]))
    distx = candidate[0] - pivot[0]
    disty = - (candidate[1] - pivot[1])
    atan = math.atan2(disty, distx)*180/math.pi
    if atan < 0:
      angle = -1 * atan + 90
    elif atan <= 90:
      angle = 90 - atan
    elif atan <= 180:
      angle = 450 - atan
    angle = round(angle, 3)
    if angle not in angles.keys():
      angles[angle] = []
    angles[angle].append((candidate[0], candidate[1]))
    print(angle)

angles_sorted = dict(sorted(angles.items(), key=lambda x: x[0], reverse=False))
#print(angles_sorted)

iter = 0
for item in angles_sorted.items():
  #print(item)
  lst = sorted(item[1], key=lambda x: math.hypot(20-x[0], 20-x[1]))
  if len(lst) == 0:
    continue
  rem = lst.pop()
  print("Angle: "+str(item[0])+", Blast #"+str(iter+1)+": "+str(rem))
  if len(lst) > 0:
    angles_sorted[item[0]] = lst
    #print("storing reduced list")
  else:
    angles_sorted[item[0]] = []
  iter += 1

print(angles_sorted)
