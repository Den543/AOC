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

# Directional Key
# up = 1
# right = 2
# down = 3
# left = 4

iRow = 65
iCol = 85
dirs = {"up":'U', "right":'R', "down":'D', "left":'L'}

visited = 0
looped = 0
exitedL = 0
exitedR = 0
exitedU = 0
exitedD = 0

def checkAll():
	global inputList
	
	y=0
	while y < len(inputList):
		x=0
		while x < len(inputList[0]):
			thisInput = createNewInput(y,x)
			print('checking: '+str(y)+" "+str(x))
			finishedRun = runOnOne(thisInput)
			#genPrintOutput(finishedRun)
			x+=1
		y+=1

def checkOne():
	thisInput = createNewInput(10,13)
	finishedRun = runOnOne(thisInput)
	genPrintOutput(finishedRun)



def runOnOne(thisInput):
	global looped
	direc = 'U'
	startRow = 65
	startCol = 85
	y=startRow
	x=startCol
	traversed = 0
	#print(thisInput[startRow][startCol])
	while y < 130:
		while x < 130:
			#set current place to whichever direction guard is traveling
			traversed+=1
			if traversed > 10000:
				looped+=1
				return(thisInput)
			#print(direc)

			#check the next space depending on which direction guard is traveling
			if direc == 'U':
				thisInput[y][x] = direc
				if y == 0:
					print("exiting Up next turn")
					return(thisInput)
				elif thisInput[y-1][x] == '#':
					direc = 'R'
				elif thisInput[y-1][x] == 'U':
					print("loop detected")
					looped += 1
					return(thisInput)
				elif thisInput[y-1][x] == '.' or 'R' or 'D' or 'L':
					y-=1
					pass


			if direc == 'R':
				thisInput[y][x] = direc
				if x == 129:
					print("exiting Right next turn")
					return(thisInput)
				elif thisInput[y][x+1] == '#':
					direc = 'D'
				elif thisInput[y][x+1] == 'R':
					print("loop detected")
					looped += 1
					return(thisInput)
				elif thisInput[y][x+1] == '.' or 'U' or 'D' or 'L':
					x+=1
					pass



			if direc == 'D':
				thisInput[y][x] = direc
				if y == 129:
					print("exiting Down next turn")
					return(thisInput)
				elif thisInput[y+1][x] == '#':
					direc = 'L'
				elif thisInput[y+1][x] == 'D':
					print("loop detected")
					looped += 1
					return(thisInput)
				elif thisInput[y+1][x] == '.' or 'R' or 'U' or 'L':
					y+=1
					pass


			if direc == 'L':
				thisInput[y][x] = direc
				if x == 0:
					print("exiting Left next turn")
					return(thisInput)
				elif thisInput[y][x-1] == '#':
					direc = 'U'
				elif thisInput[y][x-1] == 'L':
					print("loop detected")
					looped += 1
					return(thisInput)
				elif thisInput[y][x-1] == '.' or 'U' or 'D' or 'R':
					x-=1
					pass


			

			#in case of loop early on
			#return(thisInput)


	return(thisInput)




def createNewInput(y, x):
	global inputList
	thisInput=[]
	#print(y)
	#print(x)
	for line in inputList:
		thisLineList=[]
		for char in line:
			thisLineList.append(char)
		thisInput.append(thisLineList)
	print(thisInput[y][x])
	if thisInput[y][x] == '.':	
		thisInput[y][x] = '#'	
	print(thisInput[y][x])
	return(thisInput)	





def genPrintOutput(thisInput):
	outputList = []
	for line in thisInput:
		line = "".join(line)
		outputList.append(line)
	print(outputList)
















checkOne()
#checkAll()
#genPrintOutput()
print(looped)



#i think its working until the starting point gets fucked by the change