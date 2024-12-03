import os
import sys
import re
inputFile = open("./inputFile.txt", "r").read()

matches = re.findall((r'mul\([\d]+\,[\d]+\)|don\'t\(\)|do\(\)'), inputFile)

enabled = True
total = 0
for entry in matches:
	entry = str(entry)
	if entry == "don't()":
		enabled = False
	if entry == "do()":
		enabled = True
	if enabled == True:
		if entry != "do()":
			two = re.findall(r'[\d]+', entry)
			tempAnswer = int(two[0])*int(two[1])
			total+=tempAnswer
print(total)