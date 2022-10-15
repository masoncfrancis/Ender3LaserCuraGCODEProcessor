
# Author: Mason Francis
# This is a basic script to turn the laser on and off

import sys

if __name__ == '__main__':
    # Prompt for destination file path
    destinationPath = input("Please enter destination file path (any existing file will be overwritten): ")
    sourceFile = open(sys.argv[1])
    destFile = open(destinationPath, "w")
    previousLine = ['G0']
    for line in sourceFile:
        splitLine = line.split()
        try:
            test = splitLine[0]
        except:
            break
        splitG1 = splitLine[0] == 'G1'
        splitG0 = splitLine[0] == 'G0'
        prevG1 = previousLine[0] == 'G1'
        prevG0 = previousLine[0] == 'G0'
        if splitG1 and prevG0:
            destFile.write("M106\n")
            previousLine = splitLine
        elif splitLine[0] == 'G0' and previousLine[0] == 'G1':
            destFile.write("M107\n")
            previousLine = splitLine
        destFile.write(line)

    print("File processed successfully. Exiting...")
    
            