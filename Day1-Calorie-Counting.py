
## need to import the file of calories and format it to a list of lists
def formatInput(filename):
	file = open(filename)
	calorieList = [[]]
	x = 0
	for line in file:
		## run down the file, if it's not an empty line then add to a list
		line = line.rstrip()
		if line:
			calorieList[x].append(int(line))
		else:
			calorieList.append([])
			x+=1
	return calorieList

formattedList = formatInput("calories.txt")
#formattedList = formatInput("testCals.txt")

def mostCalories(calorieList):
	mostCalories = 0
	for rations in formattedList:
		totalCalories = 0
		for calories in rations:
			totalCalories += calories
			if totalCalories > mostCalories:
				mostCalories = totalCalories

def calorieRank(calorieList, count):
	calorieRanking = list(range(count))
	for rations in formattedList:
		totalCalories = 0
		for calories in rations:
			totalCalories += calories
			## we've added the total calories of the elf's rations bag
			## now we compare to the values in the calorie ranking
			for i in range(count):
				## compare to the 
				if totalCalories > calorieRanking[i]: 
					displacedValue = calorieRanking.pop(i)
					calorieRanking.insert(i, totalCalories)
					totalCalories = displacedValue
	return calorieRanking


def combinedLeaders(calorieList):
	totalCalories = 0
	for i in calorieList:
		totalCalories+=i 
	return totalCalories

ranking = calorieRank(formattedList, 3)
totalCals = combinedLeaders(ranking)
print(totalCals)