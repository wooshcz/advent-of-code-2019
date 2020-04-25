
def resizeMemory(intcode, addr):
  while len(intcode)-1 < addr:
    intcode.append(0)
  return intcode

def program(intcode):
  nextind = -1
  oldcode = 0
  index = -1
  inpcnt = 0
  relbase = 0

  while True:
    if nextind > -1:
      index = nextind
      nextind = -1
    else:
      index += 1
    #print("Index: "+str(index))

    code = intcode[index]
    strcode = str(code).zfill(5)
    opcode = int(strcode[-2:])
    if opcode == 99:
      #print("haltcode")
      break

    mode = strcode[0:-2]
    print(mode + " | " + str(opcode))
    mode1 = int(mode[2])
    mode2 = int(mode[1])
    mode3 = int(mode[0])
    arg1pos = intcode[index+1]
    arg2pos = intcode[index+2]
    arg3pos = intcode[index+3]
    if opcode in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      if mode1 == 1:
        arg1 = arg1pos
      elif mode1 == 2:
        arg1pos = relbase+arg1pos
        if arg1pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg1pos)
        arg1 = intcode[arg1pos]
      else:
        if arg1pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg1pos)
        arg1 = intcode[arg1pos]
    if opcode in [1, 2, 5, 6, 7, 8]:
      if mode2 == 1:
        arg2 = arg2pos
      elif mode2 == 2:
        arg2pos = relbase+arg2pos
        if arg2pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg2pos)
        arg2 = intcode[arg2pos]
      else:
        if arg2pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg2pos)
        arg2 = intcode[arg2pos]
    if opcode in [1, 2, 7, 8]:
      if mode3 == 1:
        arg3 = arg3pos
      elif mode3 == 2:
        arg3pos = relbase+arg3pos
        if arg3pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg3pos)
        arg3 = intcode[arg3pos]
      else:
        if arg3pos > len(intcode)-1:
          intcode = resizeMemory(intcode, arg3pos)
        arg3 = intcode[arg3pos]

    if opcode == 1:
      #print("addition of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
      if arg3pos > len(intcode)-1:
        intcode = resizeMemory(intcode, arg3pos)
      intcode[arg3pos] = arg1 + arg2
      nextind = index+4

    elif opcode == 2:
      #print("multiplication of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
      if arg3pos > len(intcode)-1:
        intcode = resizeMemory(intcode, arg3pos)
      intcode[arg3pos] = arg1 * arg2
      nextind = index+4

    elif opcode == 3:
      value = input("Enter single integer value: ")
      if arg1pos > len(intcode)-1:
        intcode = resizeMemory(intcode, arg1pos)
      intcode[arg1pos] = int(value)
      nextind = index+2
      inpcnt += 1

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
      if arg3pos > len(intcode)-1:
        intcode = resizeMemory(intcode, arg3pos)
      if arg1 < arg2:
        intcode[arg3pos] = 1
      else:
        intcode[arg3pos] = 0
      nextind = index+4

    # 1st equals 2nd
    elif opcode == 8:
      if arg3pos > len(intcode)-1:
        intcode = resizeMemory(intcode, arg3pos)
      if arg1 == arg2:
        intcode[arg3pos] = 1
      else:
        intcode[arg3pos] = 0
      nextind = index+4
    
    elif opcode == 9:
      relbase = relbase+arg1
      print("Relbase: "+str(relbase))
      nextind = index+2

    else:
      print("error")
      print(intcode)
      break

intcode = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,25,0,1016,1102,760,1,1023,1102,1,20,1003,1102,1,22,1015,1102,1,34,1000,1101,0,32,1006,1101,21,0,1017,1102,39,1,1010,1101,30,0,1005,1101,0,1,1021,1101,0,0,1020,1102,1,35,1007,1102,1,23,1014,1102,1,29,1019,1101,767,0,1022,1102,216,1,1025,1102,38,1,1011,1101,778,0,1029,1102,1,31,1009,1101,0,28,1004,1101,33,0,1008,1102,1,444,1027,1102,221,1,1024,1102,1,451,1026,1101,787,0,1028,1101,27,0,1018,1101,0,24,1013,1102,26,1,1012,1101,0,36,1002,1102,37,1,1001,109,28,21101,40,0,-9,1008,1019,41,63,1005,63,205,1001,64,1,64,1105,1,207,4,187,1002,64,2,64,109,-9,2105,1,5,4,213,1106,0,225,1001,64,1,64,1002,64,2,64,109,-9,1206,10,243,4,231,1001,64,1,64,1105,1,243,1002,64,2,64,109,-3,1208,2,31,63,1005,63,261,4,249,1106,0,265,1001,64,1,64,1002,64,2,64,109,5,21108,41,41,0,1005,1012,287,4,271,1001,64,1,64,1105,1,287,1002,64,2,64,109,6,21102,42,1,-5,1008,1013,45,63,1005,63,307,1105,1,313,4,293,1001,64,1,64,1002,64,2,64,109,-9,1201,0,0,63,1008,63,29,63,1005,63,333,1106,0,339,4,319,1001,64,1,64,1002,64,2,64,109,-13,2102,1,4,63,1008,63,34,63,1005,63,361,4,345,1105,1,365,1001,64,1,64,1002,64,2,64,109,5,1201,7,0,63,1008,63,33,63,1005,63,387,4,371,1105,1,391,1001,64,1,64,1002,64,2,64,109,7,1202,1,1,63,1008,63,32,63,1005,63,411,1105,1,417,4,397,1001,64,1,64,1002,64,2,64,109,20,1205,-7,431,4,423,1106,0,435,1001,64,1,64,1002,64,2,64,109,2,2106,0,-3,1001,64,1,64,1105,1,453,4,441,1002,64,2,64,109,-7,21101,43,0,-9,1008,1014,43,63,1005,63,479,4,459,1001,64,1,64,1105,1,479,1002,64,2,64,109,-5,21108,44,43,0,1005,1018,495,1105,1,501,4,485,1001,64,1,64,1002,64,2,64,109,-7,1205,9,517,1001,64,1,64,1105,1,519,4,507,1002,64,2,64,109,11,1206,-1,531,1106,0,537,4,525,1001,64,1,64,1002,64,2,64,109,-15,1208,0,36,63,1005,63,557,1001,64,1,64,1106,0,559,4,543,1002,64,2,64,109,7,2101,0,-7,63,1008,63,35,63,1005,63,581,4,565,1106,0,585,1001,64,1,64,1002,64,2,64,109,-3,21107,45,46,4,1005,1015,607,4,591,1001,64,1,64,1105,1,607,1002,64,2,64,109,-16,2102,1,10,63,1008,63,31,63,1005,63,631,1001,64,1,64,1106,0,633,4,613,1002,64,2,64,109,1,2107,33,10,63,1005,63,649,1106,0,655,4,639,1001,64,1,64,1002,64,2,64,109,17,2101,0,-9,63,1008,63,31,63,1005,63,679,1001,64,1,64,1106,0,681,4,661,1002,64,2,64,109,-6,2107,34,0,63,1005,63,703,4,687,1001,64,1,64,1106,0,703,1002,64,2,64,109,5,1207,-5,34,63,1005,63,719,1105,1,725,4,709,1001,64,1,64,1002,64,2,64,109,-15,1202,6,1,63,1008,63,20,63,1005,63,751,4,731,1001,64,1,64,1105,1,751,1002,64,2,64,109,21,2105,1,5,1001,64,1,64,1106,0,769,4,757,1002,64,2,64,109,5,2106,0,5,4,775,1001,64,1,64,1106,0,787,1002,64,2,64,109,-27,1207,4,35,63,1005,63,809,4,793,1001,64,1,64,1106,0,809,1002,64,2,64,109,13,2108,33,-1,63,1005,63,831,4,815,1001,64,1,64,1106,0,831,1002,64,2,64,109,4,21107,46,45,1,1005,1014,851,1001,64,1,64,1105,1,853,4,837,1002,64,2,64,109,3,21102,47,1,-3,1008,1013,47,63,1005,63,875,4,859,1106,0,879,1001,64,1,64,1002,64,2,64,109,-9,2108,28,2,63,1005,63,895,1106,0,901,4,885,1001,64,1,64,4,64,99,21101,27,0,1,21102,1,915,0,1106,0,922,21201,1,59074,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1105,1,922,21201,1,0,-1,21201,-2,-3,1,21102,1,957,0,1105,1,922,22201,1,-1,-2,1106,0,968,22102,1,-2,-2,109,-3,2105,1,0]

# tests
#intcode = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#intcode = [1102,34915192,34915192,7,4,7,99,0]

program(intcode)

