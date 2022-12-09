## parse strategy guide 

## A Y
## B X
## C Z

import pandas as pd

def strategyGuideParser(filename):
	# This opens a handle to your file, in 'r' read mode
	file_handle = open(filename, 'r')
	# Read in all the lines of your file into a list of lines
	lines_list = file_handle.readlines()
	# Do a double-nested list comprehension to get the rest of the data into your matrix
	my_data = [[val for val in line.split()] for line in lines_list[0:]]

	return my_data 

def rulesEngine():
	df=pd.DataFrame({"X":["D", "L", "W"],
					 "Y":["W", "D", "L"],
					 "Z":["L", "W", "D"]
	})
	df.index = ["A", "B", "C"]
	return df

def pointsCalculator(df, strat):
	points = 0
	for i in strat:
		result = df.loc[i[0], i[1]]
		if result in ("D"):
			points+=3
		if result in ("W"):
			points+=6
		if i[1] in ("X"):
			points+=1
		if i[1] in ("Y"):
			points+=2
		if i[1] in ("Z"):
			points+=3
	return points 


def p2PointsCalculator(df, strat):
	points = 0
	for i in strat: 
		if i[1] in ("X"):
			outcome = "L"
		if i[1] in ("Y"):
			outcome = "D"
			points+=3
		if i[1] in ("Z"):
			outcome = "W"
			points+=6
		column = df.columns[df.loc[i[0]].eq(outcome,axis=0)].tolist()
		result = "".join(column)
		if result in ("X"):
			points+=1
		if result in ("Y"):
			points+=2
		if result in ("Z"):
			points+=3
	return points 
	

## Part 1 Challenge: 

#parsedGuide = strategyGuideParser("basicStrat.txt")
parsedGuide = strategyGuideParser("AdvancedStrat.txt")
dataFrame = rulesEngine()
#points = pointsCalculator(dataFrame, parsedGuide)
points = p2PointsCalculator(dataFrame, parsedGuide)

print(points)

# rules
#Results of round 1: 4
#Results of round 2: 9
#Results of round 3: 15

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).



#- 			X(rock) Y(paper) Z(scissor)

#A(rock)       d 		w		  l

#B(paper)	   l		d 		  w

#C(scissor)	   w        l 		  d





