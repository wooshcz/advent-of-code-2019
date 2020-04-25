import math

class Planet():

  def __init__(self, pos):
    self.posx = pos[0]
    self.posy = pos[1]
    self.posz = pos[2]
    self.velx = 0
    self.vely = 0
    self.velz = 0

  def step(self):
    self.posx += self.velx
    self.posy += self.vely
    self.posz += self.velz

  def getPos(self):
    return (self.posx, self.posy, self.posz)
  
  def getVelocity(self):
    return (self.velx, self.vely, self.velz)
  
  def getEnergy(self):
    pot = abs(self.posx) + abs(self.posy) + abs(self.posz)
    kin = abs(self.velx) + abs(self.vely) + abs(self.velz)
    return kin*pot
  
  def updateVelocities(self, vel):
    if len(vel) != 3:
      return False
    else:
      self.velx += vel[0]
      self.vely += vel[1]
      self.velz += vel[2]

def applyGravity(moons):
  x = 1
  for pivot in moons:
    x1, y1, z1 = pivot.getPos()
    for candidate in moons[x:]:
      x2, y2, z2 = candidate.getPos()
      dx1 = 0
      dx2 = 0
      dy1 = 0
      dy2 = 0
      dz1 = 0
      dz2 = 0
      if x1 > x2:
        dx1 = -1
        dx2 = 1
      elif x1 < x2:
        dx1 = 1
        dx2 = -1
      if y1 > y2:
        dy1 = -1
        dy2 = 1
      elif y1 < y2:
        dy1 = 1
        dy2 = -1
      if z1 > z2:
        dz1 = -1
        dz2 = 1
      elif z1 < z2:
        dz1 = 1
        dz2 = -1
      pivot.updateVelocities((dx1, dy1, dz1))
      candidate.updateVelocities((dx2, dy2, dz2))
    x += 1

def applyVelocity(moons):
  for moon in moons:
    moon.step()

def findCycle(moons, coord, initial_state):
  step = 0
  state = ()
  refstate = (
    initial_state[0][coord], 0,
    initial_state[1][coord], 0,
    initial_state[2][coord], 0,
    initial_state[3][coord], 0
    )
  while state != refstate:
    if (step+1) % 10000 == 0:
      print("Step #%d" % (step+1))
    applyGravity(moons)
    applyVelocity(moons)
    state = ()
    for moon in moons:
      pos = moon.getPos()
      vel = moon.getVelocity()
      state = state + (pos[coord], vel[coord])
    step += 1
  return step

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

moons = [
  Planet((17, 5, 1)),
  Planet((-2, -8, 8)),
  Planet((7, -6, 14)),
  Planet((1, -10, 4))
]

for step in range(0, 1000):
  print("Step #%d" % (step+1))
  applyGravity(moons)
  applyVelocity(moons)


i = 1
total = 0
for moon in moons:
  print(moon.getPos())
  print(moon.getVelocity())
  energy = moon.getEnergy()
  total += energy
  print("Energy of moon #%d: %f" % (i, energy))
  i += 1

print(total)

moons = (Planet((17, 5, 1)), Planet((-2, -8, 8)), Planet((7, -6, 14)), Planet((1, -10, 4)))

initial_state = (
  (17,5,1),
  (-2,-8,8),
  (7,-6,14),
  (1,-10,4)
)

state = []
cy1 = findCycle(moons, 0, initial_state)
moons = (Planet((17, 5, 1)), Planet((-2, -8, 8)), Planet((7, -6, 14)), Planet((1, -10, 4)))
cy2 = findCycle(moons, 1, initial_state)
moons = (Planet((17, 5, 1)), Planet((-2, -8, 8)), Planet((7, -6, 14)), Planet((1, -10, 4)))
cy3 = findCycle(moons, 2, initial_state)

print("Cycle X:" + str(cy1))
print("Cycle Y:" + str(cy2))
print("Cycle Z:" + str(cy3))

lcmxy = lcm(cy1, cy2)
lcmxyz = lcm(lcmxy, cy3)

print(lcmxyz)
