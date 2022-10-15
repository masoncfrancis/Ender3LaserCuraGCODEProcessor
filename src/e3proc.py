
# Author: Mason Francis
# This is a basic script to turn the laser on and off

import sys

if __name__ == '__main__':
    # Prompt for destination file path
    destinationPath = input("Please enter destination file path (any existing file will be overwritten): ")
    sourceFile = open(sys.argv[1])
    destFile = open(destinationPath, "w")
    previousLine = ["G0"]
    for line in sourceFile:
        splitLine = line.split()
        if splitLine[0] == "G1" and previousLine[0] == "GO":
            destFile.write("M106")
            previousLine = splitLine
        elif splitLine[0] == "G0" and previousLine[0] == "G1":
            destFile.write("M107")
            previousLine = splitLine
        destFile.write(line)
    
            