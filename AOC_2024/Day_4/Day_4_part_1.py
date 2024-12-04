inputFile = open("./inputFile.txt", "r")
inputList = []

for line in inputFile:
	lineList = []
	line = line.strip('\n')
	for char in line:
		lineList.append(char)
	inputList.append(lineList)

print(inputFile)
print(inputList)


totalXMAS = 0
lineIndex = 0

#direction counter because something is off
up = 0
down = 0
forward = 0
backward = 0
upLeft = 0
upRight = 0
downLeft = 0
downRight = 0



for lineList in inputList:
	charIndex = 0
	for char in lineList:
		if char == 'X':
			#check all directions for XMAS
			
			#forwards	

			if charIndex < 137: 
				if inputList[lineIndex][charIndex+1] == 'M' and inputList[lineIndex][charIndex+2] == 'A' and inputList[lineIndex][charIndex+3] == 'S':
					totalXMAS+=1
					forward+=1
				#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex+1]+inputList[lineIndex][charIndex+2]+inputList[lineIndex][charIndex+3])

		#backwards	
			if charIndex > 2: 
				if inputList[lineIndex][charIndex-1] == 'M' and inputList[lineIndex][charIndex-2] == 'A' and inputList[lineIndex][charIndex-3] == 'S':
					totalXMAS+=1
					backward+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3]+" at "+str(lineIndex)+"-"+str(charIndex))

			#up

			if lineIndex > 2:
				if inputList[lineIndex-1][charIndex] == 'M' and inputList[lineIndex-2][charIndex] == 'A' and inputList[lineIndex-3][charIndex] == 'S':
					totalXMAS+=1
					up+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex+1]+inputList[lineIndex][charIndex+2]+inputList[lineIndex][charIndex+3])


			#down

			if lineIndex < 137:
				if inputList[lineIndex+1][charIndex] == 'M' and inputList[lineIndex+2][charIndex] == 'A' and inputList[lineIndex+3][charIndex] == 'S':
					totalXMAS+=1
					down+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3])


			#diagonal up left

			if lineIndex > 2 and charIndex > 2:
				if inputList[lineIndex-1][charIndex-1] == 'M' and inputList[lineIndex-2][charIndex-2] == 'A' and inputList[lineIndex-3][charIndex-3] == 'S':
					totalXMAS+=1
					upLeft+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3])


			#diagonal up right

			if lineIndex > 2 and charIndex < 137:	
				if inputList[lineIndex-1][charIndex+1] == 'M' and inputList[lineIndex-2][charIndex+2] == 'A' and inputList[lineIndex-3][charIndex+3] == 'S':
					totalXMAS+=1
					upRight+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3])


			#diagonal down left

			if lineIndex < 137 and charIndex > 2:
				if inputList[lineIndex+1][charIndex-1] == 'M' and inputList[lineIndex+2][charIndex-2] == 'A' and inputList[lineIndex+3][charIndex-3] == 'S':
					totalXMAS+=1
					downLeft+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3])


			#diagonal down right

			if lineIndex < 137 and charIndex < 137:
													# I had this +3+3 pair set as +2+3 for a long time, throwing off the answer    \/
				if inputList[lineIndex+1][charIndex+1] == 'M' and inputList[lineIndex+2][charIndex+2] == 'A' and inputList[lineIndex+3][charIndex+3] == 'S':
					totalXMAS+=1
					downRight+=1
					#print("found "+inputList[lineIndex][charIndex]+inputList[lineIndex][charIndex-1]+inputList[lineIndex][charIndex-2]+inputList[lineIndex][charIndex-3])




		charIndex += 1
	lineIndex += 1



#print(len(inputList))
#print(inputList)
print(totalXMAS)
print(up)
print(down)
print(forward)
print(backward)
print(upLeft)
print(upRight)
print(downLeft)
print(downRight) #I finally noticed this was 150 when all other diagonals were mid 400's ^^ see other note
