import os
import sys
import re


inputFile = open("./inputFile.txt", "r")

varleft = []
varright = []

for line in inputFile:
	print(line)
	matches = re.findall(r"\d+", line)
	varleft.append(int(matches[0]))
	varright.append(int(matches[1]))


varleft.sort()
varright.sort()
print(varleft)
index = 0
total = 0
for item in varleft:
	diff = varleft[index] - varright[index]
	print(diff)
	total += abs(diff)
	index+=1
print("total: " + str(total))