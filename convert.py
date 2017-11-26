# Creators: Stephanie Fu
# 26 November 2017
import sys

def stripComments(line):
    stripped = line.split(" ")
    for el in range(len(stripped)):
      if stripped[el][0] == '#':
        for i in range(len(stripped) - el): stripped.pop()
        return stripped

def readFile(fileName):
    lineNumber = 1
    with open(fileName) as fp:
      for line in fp:
        processLine(fileName, line, lineNumber)
        lineNumber+=1

def processLine(readFileName, line, lineNumber):
    columns = stripComments(line)
    writeFile(readFileName, columns, lineNumber)

def getData(columns):
    values = []
    for a in columns[2:]:
        data = a.split(":")[1]
        values.append(data)
    return values

def countLines(fileName):
    lines = 0
    with open(fileName) as fp:
        for line in fp:
            lines += 1
    return lines

def writeFile(readFileName, columns, lineNumber):
    lines = countLines(readFileName)
    root = readFileName[:len(readFileName)-4]
    data = getData(columns)
    writeFileName = root + "-new.csv"
    if lineNumber == 1:
        with open(writeFileName, "w+"): pass
    with open(writeFileName, "a+") as f:
        sys.stdout.write('\r')
        if lineNumber == 1:
            f.write(str(lines) + ",")
            f.write(str(len(data)) + ",")
            f.write("NONE, LOW, HIGH\n")
        f.write(",".join(data) + "\n")
        sys.stdout.write(" " + str(int((lineNumber / lines) * 100)) + "%")
        sys.stdout.flush()

readFile(sys.argv[1])