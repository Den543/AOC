import os
import sys
import re
import itertools
inputFile = open("./inputFile.txt", "r")
inputListTotal = []
inputListOps = []
total=0

def genIn():
	global inputFile
	global inputListTotal
	global inputListOps
	opsList = []
	for line in inputFile:
		line = line.strip('\n')
		matches = re.findall(r'\d+', line)
		inputListTotal.append(int(matches[0]))
		opsList = []
		for i in matches:
			if i == matches[0]:
				pass
			else:
				opsList.append(int(i))
		inputListOps.append(opsList)




def run():
	global inputListTotal
	global inputListOps
	global total
	index = 0
	listToTotal =[]
	for t in inputListTotal:
		allPoss = genAllPossOps(len(inputListOps[index])-1)
		for sublist in allPoss:	
			i = 0
			subt = inputListOps[index][i]
			for op in sublist:		
				if op == '+':
					subt += inputListOps[index][i+1]
				elif op == '*':
					subt *=	inputListOps[index][i+1]
				i+=1
			if subt == t:
				print("found solution")	
				print(t)
				print(inputListOps[index])
				print(sublist)
				total+=t
				break
		index+=1
		

def genAllPossOps(n):
	allPoss = list(itertools.product('+*', repeat=n))
	return(allPoss)



genIn()
run()
print("Total of calibration results: "+str(total))