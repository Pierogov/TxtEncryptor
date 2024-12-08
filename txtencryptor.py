import sys
fileName = sys.argv[1]
try:
    f = open(format(fileName), "r+")
    fileContent = f.read();
    fileContent = list(fileContent.encode('ascii'))
    for i in range(len(fileContent)):
        fileContent[i] = fileContent[i] + 3
    print (bytes(fileContent).decode())

except:
    print("Unable to locate file!")