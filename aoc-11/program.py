
class IntcodeComputer:

  debug = False

  def __init__(self, intcode):
    self.intcode = intcode
    self.nextind = -1
    self.storeInputTo = -1
    self.index = -1
    self.inpcnt = 0
    self.relbase = 0
    self.waitForInput = False
    self.isRunning = False
    self.outbuffer = []

  def isRunning(self):
    return self.isRunning

  def isWaitingForInput(self):
    return self.waitForInput

  def resizeMemory(self, addr):
    while len(self.intcode)-1 < addr:
      self.intcode.append(0)

  def readBuffer(self):
    if len(self.outbuffer) > 0:
      result, self.outbuffer = self.outbuffer, []
      return result
    else:
      return []

  def writeInput(self, value):
    if self.waitForInput == True and len(str(value)) > 0 and self.storeInputTo > -1:
      self.intcode[self.storeInputTo] = int(value)
      self.waitForInput = False
      self.storeInputTo = -1
      print("Value %d was stored to the computer and program resumed" % (int(value)))
      self.run()
      return 0
    else:
      print("Value was refused!")
      return 1

  def run(self):
    self.isRunning = True

    while True:
      if self.nextind > -1:
        self.index = self.nextind
        self.nextind = -1
      else:
        self.index += 1
      if self.debug == True:
        print("Index: "+str(self.index))

      code = self.intcode[self.index]
      strcode = str(code).zfill(5)
      opcode = int(strcode[-2:])
      if opcode == 99:
        if self.debug == True:
          print("haltcode")
        self.isRunning = False
        return 0

      mode = strcode[0:-2]
      if self.debug == True:
        print(mode + " | " + str(opcode))
      mode1 = int(mode[2])
      mode2 = int(mode[1])
      mode3 = int(mode[0])
      arg1pos = self.intcode[self.index+1]
      arg2pos = self.intcode[self.index+2]
      arg3pos = self.intcode[self.index+3]
      if opcode in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if mode1 == 1:
          arg1 = arg1pos
        elif mode1 == 2:
          arg1pos = self.relbase+arg1pos
          if arg1pos > len(self.intcode)-1:
            self.resizeMemory(arg1pos)
          arg1 = self.intcode[arg1pos]
        else:
          if arg1pos > len(self.intcode)-1:
            self.resizeMemory(arg1pos)
          arg1 = self.intcode[arg1pos]
      if opcode in [1, 2, 5, 6, 7, 8]:
        if mode2 == 1:
          arg2 = arg2pos
        elif mode2 == 2:
          arg2pos = self.relbase+arg2pos
          if arg2pos > len(self.intcode)-1:
            self.resizeMemory(arg2pos)
          arg2 = self.intcode[arg2pos]
        else:
          if arg2pos > len(self.intcode)-1:
            self.resizeMemory(arg2pos)
          arg2 = self.intcode[arg2pos]
      if opcode in [1, 2, 7, 8]:
        if mode3 == 1:
          arg3 = arg3pos
        elif mode3 == 2:
          arg3pos = self.relbase+arg3pos
          if arg3pos > len(self.intcode)-1:
            self.resizeMemory(arg3pos)
          arg3 = self.intcode[arg3pos]
        else:
          if arg3pos > len(self.intcode)-1:
            self.resizeMemory(arg3pos)
          arg3 = self.intcode[arg3pos]

      if opcode == 1:
        if self.debug == True:
          print("addition of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
        if arg3pos > len(self.intcode)-1:
          self.resizeMemory(arg3pos)
        self.intcode[arg3pos] = arg1 + arg2
        self.nextind = self.index+4

      elif opcode == 2:
        if self.debug == True:
          print("multiplication of " + str(arg1) + " and " + str(arg2) + " stored into: " + str(arg3pos))
        if arg3pos > len(self.intcode)-1:
          self.resizeMemory(arg3pos)
        self.intcode[arg3pos] = arg1 * arg2
        self.nextind = self.index+4

      elif opcode == 3:
        print("Provide single integer value: ")
        if arg1pos > len(self.intcode)-1:
          self.resizeMemory(arg1pos)
        self.nextind = self.index+2
        self.waitForInput = True
        self.storeInputTo = arg1pos
        return 0

      elif opcode == 4:
        print("Output from execution: %d" % (arg1))
        self.outbuffer.append(arg1)
        self.nextind = self.index+2

      # jump-if-true
      elif opcode == 5:
        if arg1 != 0:
          self.nextind = arg2
        else:
          self.nextind = self.index+3

      # jump-if-false
      elif opcode == 6:
        if arg1 == 0:
          self.nextind = arg2
        else:
          self.nextind = self.index+3

      # 1st less than 2nd
      elif opcode == 7:
        if arg3pos > len(self.intcode)-1:
          self.resizeMemory(arg3pos)
        if arg1 < arg2:
          self.intcode[arg3pos] = 1
        else:
          self.intcode[arg3pos] = 0
        self.nextind = self.index+4

      # 1st equals 2nd
      elif opcode == 8:
        if arg3pos > len(self.intcode)-1:
          self.resizeMemory(arg3pos)
        if arg1 == arg2:
          self.intcode[arg3pos] = 1
        else:
          self.intcode[arg3pos] = 0
        self.nextind = self.index+4
      
      elif opcode == 9:
        self.relbase = self.relbase+arg1
        if self.debug == True:
          print("Relbase: "+str(self.relbase))
        self.nextind = self.index+2

      else:
        print("error")
        print(self.intcode)
        self.isRunning = False

