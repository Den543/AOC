import os
import sys
import re
inputFile = open("./inputFile.txt", "r")
inputList = []
for line in inputFile:
	lineList = []
	line = line.strip('\n')
	matches = re.findall(r"[\d]+", line)
	inputList.append(matches)


print(inputList)




#for level in inputList:
#	for number in level:
#		number = int(number)
totalSafe = 0
totalUnsafe=0
for level in inputList:
	length = len(level)
	index = 0
	positive = False
	negative = False
	unsafe=False
	for number in level:
		if index<(length-1):
			diff = int(level[index]) - int(level[index+1])

			if abs(diff) == 0:
				unsafe = True
#				print(diff)
				break
			if abs(diff) > 3:
				unsafe = True
#				print(diff)
				break
			if diff > 0:
				positive = True
			if diff < 0:
				negative = True
			if positive == True:
				if negative == True:
					unsafe = True


		index+=1
	if unsafe == True:
		totalUnsafe+=1
	else:
		totalSafe+=1




print(len(inputList))
print("unsafe: " +str(totalUnsafe))
print("safe: " +str(totalSafe))
