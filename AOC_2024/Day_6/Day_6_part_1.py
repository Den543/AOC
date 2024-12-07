import os
import sys
import re
inputFile = open("./inputFile.txt", "r")
inputList = []
for line in inputFile:
	lineList = []
	line = line.strip('\n')
	for char in line:
		lineList.append(char)
	inputList.append(lineList)
#print(inputList)
i = 0
#for line in inputList:
#	for char in line:
#		i+=1
#		guard = re.search(r'\^', char)
#		if guard != None:
#			print(guard)
#			print(i)
#starting point is [65][85]
#print(inputList)
#print(inputList[65][85])
guardInArea = True
# Directional Key
# up = 1
# right = 2
# down = 3
# left = 4

iRow = 65
iCol = 85
direction = 1

def moveOneSpace():
	global guardInArea
	global inputList
	global iRow
	global iCol
	global direction
	if direction == 1:
		try:
			inputList[iRow][iCol] = 'X'		
			if inputList[iRow-1][iCol] == '.' or 'X':

				iRow-=1
			if inputList[iRow-1][iCol] == ('#'):
				direction=2
			return(True)
		except:
			print('exited up')
			return(False)

	if direction == 2:
		try:
			inputList[iRow][iCol] = 'X'
			if inputList[iRow][iCol+1] == '.' or 'X':
				iCol+=1
			if inputList[iRow][iCol+1] == '#':
				direction=3
			return(True)
		except:
			print('exited right')
			return(False)

	if direction == 3:
		try:
			inputList[iRow][iCol] = 'X'			
			if inputList[iRow+1][iCol] == '.' or 'X':
				iRow+=1
			if inputList[iRow+1][iCol] == '#':
				direction=4
			return(True)
		except:
			print('exited down')
			return(False)

	if direction == 4:
		try:
			inputList[iRow][iCol] = 'X'			
			if inputList[iRow][iCol-1] == '.' or 'X':
				if iCol > 0:	
					iCol-=1
				else:
					return(False)
			if inputList[iRow][iCol-1] == '#':
				if iCol > 0:	
					direction = 1
				else:
					return(False)
			return(True)
		except:
			print('exited left')
			return(False)




while guardInArea == True:
	guardInArea = moveOneSpace()


outputList = []

for line in inputList:
	a = "".join(line)
	outputList.append(a)

print(outputList)
total = 0
for line in outputList:
	matches = re.findall('X', line)
	#print(matches)
	total += len(matches)
	#print(len(matches))
print(total)
print(inputList[65][85])