import argparse

parser = argparse.ArgumentParser(prog="TXTEncryptor", description="Encrypts .txt files")
parser.add_argument("fileName", type=str, help="Path to input file")
parser.add_argument("-o", "--output", type=str, help="Path to output file")
parser.add_argument("-d", "--decrypt", type=bool, help="Set to true, if you want to decrypt the file")
args = parser.parse_args()

fileName = args.fileName
outputFile = args.output
decryptBool = args.decrypt

try:
    f = open(fileName, "r")
    fileContent = f.read();
    fileContent = list(fileContent.encode('ascii'))
    
    for i in range(len(fileContent)):
        if(decryptBool!=True):
            fileContent[i] = fileContent[i] + 3
        else:
            fileContent[i] = fileContent[i] - 3
    f.close();
    try:
        f = open(outputFile, "w")
        f.write(bytes(fileContent).decode());
        if(decryptBool!=True):
            print("Encrypted content saved to: " + outputFile)
        else:
            print("Decrypted content saved to: " + outputFile)
        f.close()
    except:
        if(decryptBool!=True):
            print("Encrpyted content: " + bytes(fileContent).decode())
        else:
            print("Decrpyted content: " + bytes(fileContent).decode())

except:
    print("Error: Unable to locate input file!")