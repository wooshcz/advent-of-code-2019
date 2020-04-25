import math

intcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

print("length: "+str(len(intcode)))
nextcode = 0
oldcode = 0

for index in range(0, len(intcode)-1):
  
  code = intcode[index]
  arg1pos = intcode[index+1]
  arg2pos = intcode[index+2]
  respos = intcode[index+3]
  if nextcode > index:
    continue

  if code == 1:
    print("addition of " + str(intcode[arg1pos]) + " and " + str(intcode[arg2pos]) + " stored into: " + str(respos))
    oldcode = intcode[respos]
    intcode[respos] = intcode[arg1pos] + intcode[arg2pos]
    print(str(oldcode) + " --> " + str(intcode[respos]))
    nextcode = index+4

  if code == 2:
    print("multiplication of " + str(intcode[arg1pos]) + " and " + str(intcode[arg2pos]) + " stored into: " + str(respos))
    oldcode = intcode[respos]
    intcode[respos] = intcode[arg1pos] * intcode[arg2pos]
    print(str(oldcode) + " --> " + str(intcode[respos]))
    nextcode = index+4

  if code == 99:
    print("haltcode")
    break
  

print(intcode)

