
intcode = [3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99]

nextind = 0
oldcode = 0
index = -1

while True:
  if nextind > 0:
    index = nextind
    nextind = 0
  else:
    index += 1
  print("Index: "+str(index))

  code = intcode[index]
  strcode = str(code).zfill(5)
  opcode = int(strcode[-2:])
  if opcode == 99:
    print("haltcode")
    break

  mode = strcode[0:-2]
  print(mode + " | " + str(opcode))
  mode1 = int(mode[2])
  mode2 = int(mode[1])
  mode3 = int(mode[0])
  arg1pos = intcode[index+1]
  arg2pos = intcode[index+2]
  arg3pos = intcode[index+3]
  if opcode in [1, 2]:
    arg3 = intcode[arg3pos]
  if opcode in [1, 2, 4, 5, 6, 7, 8]:
    if mode1 == 1:
      arg1 = arg1pos
    else:
      arg1 = intcode[arg1pos]
  if opcode in [1, 2, 5, 6, 7, 8]:
    if mode2 == 1:
      arg2 = arg2pos
    else:
      arg2 = intcode[arg2pos]

  if opcode == 1:
    #print("addition of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
    oldcode = arg3
    intcode[arg3pos] = arg1 + arg2
    #print(str(oldcode) + " --> " + str(intcode[arg3pos]))
    nextind = index+4

  elif opcode == 2:
    #print("multiplication of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
    oldcode = arg3
    intcode[arg3pos] = arg1 * arg2
    #print(str(oldcode) + " --> " + str(intcode[arg3pos]))
    nextind = index+4

  elif opcode == 3:
    value = input("Enter single integer value: ")
    intcode[arg1pos] = int(value)
    nextind = index+2

  elif opcode == 4:
    print("Output from execution: %d" % (arg1))
    nextind = index+2

  # jump-if-true
  elif opcode == 5:
    if arg1 != 0:
      nextind = arg2
    else:
      nextind = index+3

  # jump-if-false
  elif opcode == 6:
    if arg1 == 0:
      nextind = arg2
    else:
      nextind = index+3

  # 1st less than 2nd
  elif opcode == 7:
    if arg1 < arg2:
      intcode[arg3pos] = 1
    else:
      intcode[arg3pos] = 0
    nextind = index+4

  # 1st equals 2nd
  elif opcode == 8:
    if arg1 == arg2:
      intcode[arg3pos] = 1
    else:
      intcode[arg3pos] = 0
    nextind = index+4

  else:
    print("error")
    break

#print(intcode)
