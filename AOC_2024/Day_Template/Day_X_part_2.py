import os
import sys
import re
inputFile = open("./inputFile.txt", "r")
inputList = []
for line in inputFile:
	line = line.strip('\n')
	inputList.append(line)