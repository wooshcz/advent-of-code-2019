import sys
import math

sys.setrecursionlimit(10**4)

stream = open('input-test3.txt', 'r', )
line = ""
reactions = {}
consumed = {}
remains = {}
for line in stream.readlines():
  [a, b] = line.split('=>')
  b = b.strip()
  a = a.strip()
  #print(line)
  #print(b.split(" "))
  [bcnt, bname] = b.split(" ")
  reactions[bname] = (int(bcnt), {})
  consumed[bname] = 0
  remains[bname] = 0
  alst = a.split(",")
  for item in alst:
    item = item.strip()
    [acnt, aname] = item.split(" ")
    reactions[bname][1][aname] = int(acnt)
consumed['ORE'] = 0
remains['ORE'] = 0

def iterateReactions(parent, amount):
  if parent in list(reactions.keys()):
    qnt = reactions[parent][0]
    parts = dict(reactions[parent][1])
    if len(parts.keys()) > 0:
      print(str(qnt) + "x " + parent + " <-- " + str(parts))
      for child in parts.keys():
        #if child in list(reactions.keys()):
          rem = remains[child]
          print(child+" remains: "+str(rem))
          needed = math.ceil(amount/qnt * parts[child])
          if rem >= needed:
            produced = 0
            remains[child] = rem-needed
          else:
            if child == 'ORE':
              mult = 1
            else:
              mult = reactions[child][0]
            produced = math.ceil(needed/mult)*mult - rem
            remains[child] += produced - needed
          print(child+" needed:" + str(needed)+" / produced: "+str(produced))
          #if remains[child] > 0:
          print(child+" new remains: "+str(remains[child]))
          if produced > 0:
            consumed[child] += produced
            iterateReactions(child, produced)

iterateReactions('FUEL', 1)

print("ORE is needed " + str(consumed['ORE']))
