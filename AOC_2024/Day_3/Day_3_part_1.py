import os
import sys
import re
inputFile = open("./inputFile.txt", "r").read()
realInstructions = 	re.findall(r'mul\([\d]+\,[\d]+\)', inputFile)
print(realInstructions)
total = 0
for a in realInstructions:
	two = re.findall(r'[\d]+', a)
	tempAnswer = int(two[0])*int(two[1])
	total+=tempAnswer
print(total)