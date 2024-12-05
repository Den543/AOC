## This one is ugly, want to rewrite when time allows





import os
import sys
import re
rules = open("./inputFile.txt", "r")
updates = open("./inputFile1.txt", "r")

rulesList = []
updatesList = []

for line in updates:
	lineList = []
	line = line.strip('\n')
	digits = re.findall(r'\d+', line)
	updatesList.append(digits)
#print(updatesList)

for line in rules:
	line = line.strip('\n')
	digits = re.findall(r'\d+', line)
	rulesList.append(digits)
	
#print(rulesList)

needsReorderedLists = []
bad = 0
total = 0

#set the  initial list for what "updateLists" break rules to needsReorderedLists
for update in updatesList:
	badOrder = False
	for rule in rulesList:
		first = None
		second = None
		try:
			first = update.index(rule[0])
		except:
			pass
		try:
			second = update.index(rule[1])
		except:
			pass
		try:
			if (first != None) and (second != None):	
				if first > second:
					badOrder = True
				elif first < second:
					pass
		except:
			pass
	if badOrder == False:
		pass
	elif badOrder == True:
		needsReorderedLists.append(update)


#print(needsReorderedLists)

print(needsReorderedLists[0])

	
def fixOneLine(i):
	badOrder = False
	for rule in rulesList:
		first = None
		second = None
		try:
			first = needsReorderedLists[i].index(rule[0])
		except:
			pass
		try:
			second = needsReorderedLists[i].index(rule[1])
		except:
			pass
		try:
			if (first != None) and (second != None):	
				if first > second:
					print("rule: "+str(rule[0])+"|"+str(rule[1]))
					needsReorderedLists[i][first], needsReorderedLists[i][second] = needsReorderedLists[i][second], needsReorderedLists[i][first]
					print("after swap: "+str(needsReorderedLists[i]))
					badOrder = True
				elif first < second:
					pass
		except:
			pass
	if badOrder == False:
		print("made it through all rules for one line")
		pass



def iterateUntilFixed():
	i=0
	while i < 110:
		print("first: ")
		fixOneLine(i)
		print("second: ")
		fixOneLine(i)
		print("third: ")
		fixOneLine(i)
		print("fourth: ")
		fixOneLine(i)
		print("fifth: ")
		fixOneLine(i)
		print("sixth: ")
		fixOneLine(i)
		i+=1

iterateUntilFixed()


for line in needsReorderedLists:
		middle = len(line)/2
		print(line[int(middle)])
		total += int(line[int(middle)])

print("total: "+str(total))
#print(len(needsReorderedLists))





#iterateThroughNeedsReordered()
#need to check every rule for each line in the needsReorderedListsList
#if rule is broken, need to swap places for those two values 
#and recheck all rules until no swap is needed 