import sys
import re

currVarInt = 0
pastVarInt = -1
currFuncStr = ""

def getFileText(path):
  f = open(path, "r")
  txt = f.read()
  f.close()
  return txt

def rmCommentsSpacing(unparsed):
  noComments = re.sub(r'#.*', '', unparsed)
  # print(noComments)
  return re.sub(r'[^1Ii!\|l\[\]]', '', noComments)

def parse1s0s(l1str):
  binStr = ""
  for c in l1str:
    if c == "1":
      binStr += "0"
    elif c == "l":
      binStr += "1"
  i = int(binStr, 2)
  return i 

def findLastI(l, i, c):
  for x in range(len(l)):
    if l[len(l) - x - 1] == c and len(l) - x - 1 < i:
      return len(l) - x - 1
  return 0

def parseCleaned(cleanedStr):
  global currFuncStr
  global pastVarInt
  global currVarInt
  l = [c for c in cleanedStr]
  for i in range(len(l)):
    c = l[i]
    if c == "[":
      pastVarInt = currVarInt
      currVarInt = parse1s0s(''.join(l[findLastI(l, i, "["):i])) 
    elif c == "]":
      currFuncStr = ''.join(l[findLastI(l, i, "]"):i]).replace("[", "")
    elif c == "I":
      sys.stdout.write(chr(currVarInt))
    elif c == "i":
      parseCleaned(currFuncStr)
    elif c == "|":
      if currVarInt != pastVarInt:
        parseCleaned(currFuncStr)
    elif c == "!":
        print(cleanedStr)
    elif c != "1" and c != "l":
      print(f"error parsing char {c}")
      sys.exit(1)

def main():
  if len(sys.argv) < 2:
    print("You need to pass a file into the interpreter")
    sys.exit(1)
  unparsed = getFileText(sys.argv[1])
  cleaned = rmCommentsSpacing(unparsed)
  parseCleaned(cleaned)

if __name__ == "__main__":
  main()
