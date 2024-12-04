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


## Part 2 same setup, but searching for A's and checking for MAS diagonals in either order
## New guards, only one extra char needed on all sides this time, not 3

for lineList in inputList:
	charIndex = 0
	for char in lineList:
		# Switch to checking for A
		if char == 'A':
			#check all A's for complete XMAS
			
			#let's do this all in one this time	
			#define the corner boundaries
			if (charIndex > 0 and charIndex < 139) and (lineIndex > 0 and lineIndex < 139): 
				if inputList[lineIndex-1][charIndex-1] == 'M' and inputList[lineIndex+1][charIndex+1] == 'S' or inputList[lineIndex-1][charIndex-1] == 'S' and inputList[lineIndex+1][charIndex+1] == 'M':
					if inputList[lineIndex+1][charIndex-1] == 'M' and inputList[lineIndex-1][charIndex+1] == 'S' or inputList[lineIndex+1][charIndex-1] == 'S' and inputList[lineIndex-1][charIndex+1] == 'M':
						totalXMAS+=1


		charIndex += 1
	lineIndex += 1


print(totalXMAS)
