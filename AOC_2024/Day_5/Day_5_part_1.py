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
	
print(rulesList)


bad = 0
total = 0
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
					#print(update)
					badOrder = True
					bad += 1
					#print("rule is: "+str(rule))
					#print(str(first)+" comes later than "+str(second))
					#break
				elif first < second:
					pass
		except:
			pass
	if badOrder == False:
		print(update)
		print(str(len(update)))
		middle = len(update)/2
		print(update[int(middle)])
		total += int(update[int(middle)])
print(str(bad))
print(str(len(updatesList)))
print("total: "+str(total))