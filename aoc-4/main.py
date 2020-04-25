
import math

start = 246540
end = 787419

def isNotDecreasing(x):
  test = str(x)
  lastn = '0'
  for n in test:
    if int(n) < int(lastn):
      return False
    lastn = n
  return True

def hasDouble(x):
  test = str(x)
  for n in test:
    if test.count(n) > 1:
      return True
  return False

def hasStrictDouble(x):
  test = str(x)
  for n in test:
    if test.count(n) == 2:
      return True
  return False

i = 0
for n in range(start, end):
  if isNotDecreasing(n) == True and hasDouble(n) and hasStrictDouble(n):
    i += 1

print(i)
