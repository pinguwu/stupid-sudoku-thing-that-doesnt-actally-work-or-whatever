# shit what
# okay uhhhhhhh
# import modules n stuff??
import math
import os
import random

# define variables n shit
# what the fuck does a sudoku table look like compressed into a line???????
# okay so the easy shit looks like a 9x9 grid, i'm gonna start with just one 3x3 square

def sudokuGridOrigin ():
	return ([0,0,3],[2,0,0],[0,0,0]) # constant variable workaround
sudokuGridManip = sudokuGridOrigin() # mainuplated variable definition
# print(sudokuGridManip) # test

numberEmpty = 0 # begin empty box count
someNumber = numberEmpty # we'll need this later
for row in sudokuGridManip: # in every row...
	for number in row: # and for every number in that row...
		if (number == 0): # check if a box is empty
			numberEmpty += 1 # if it is, increment the numberEmpty count by 1
# print(numberEmpty) # test

bruteTest = [] # begin guess definition
for x in range (0, numberEmpty): # for however many empty spaces there are in the sudoku
	bruteTest.append(1) # add a number to the guess
# print(bruteTest) # test


def testGrid (rawGrid, guess): # function definition. Takes a sudoku grid and a guess as inputs
	numSelect = 0 # guess number select
	print(rawGrid)
	print(guess)

	print(numSelect)


	outputGrid = rawGrid # output: will be modified
	print(outputGrid)

	for rowNum in range (0, len(rawGrid)): # for each row in the grid
		print ("ROWNUM -> " + str(rowNum))
		for num in range (0, len(rawGrid[rowNum])): # and for every number in that row
			print("NUM - > " + str(num))
			if (rawGrid[rowNum][num] == 0): # check if that number is 0, if so:
				print ("CHECK TRUE")
				outputGrid[rowNum][num] = guess[numSelect] # set that number in the output grid to a guess number
				numSelect += 1 # increase the guess selection
	
	return (outputGrid) # return the output grid

def checkGrid (grid):
	total = []
	for row in grid:
		for num in row:
			total.append(num)

	one = 0
	two = 0
	three = 0

	for number in total:
		if number == 1:
			one += 1
		elif number == 2:
			two += 1
		elif number == 3:
			three += 1

	if (one == 3 and two == 3 and three == 3):
		return True
	else:
		return False


def render (rawGrid):
	for line in rawGrid:
		textOutput = ""
		for number in line:
			textOutput = textOutput + str(number)

def increment (test):
	old = ""
	for number in test:
		old = old + str(number)
	old = int(old)
	old += 1

	new = [int(x) for x in str(old)]
	#rint(new)

	if (4 in new):
		while (4 in new):
			for number in range (0, len(new)):
				if (new[number] >= 4):
					if (number != 0):
						new[number] = 1
						new[number - 1] += 1
	
	## print(test)
	# print("NEW -> " + str(new))
	return(new)



def set (test):
	old = ""
	for number in test:
		old = old + str(number)
	old = int(old)
	old += 1

	new = [int(x) for x in str(old)]
	#rint(new)

	while (4 in new):
		for number in range (0, len(new)):
			if (new[number] >= 4):
				if (number != 0):
					new[number] = 0
					new[number - 1] += 1
	return(new)

loop = True

#checkGrid(testGrid([[1,2,3],[4,5,6],[7,8,9]], bruteTest))


bruteTest = set(bruteTest)

while (loop == True):
	gridGuess = testGrid(sudokuGridManip, bruteTest)
	# print(gridGuess)
	if (checkGrid(gridGuess) == True):
		render(gridGuess)
		loop = False
		break

	if (loop == False):
		break

	bruteTest = increment(bruteTest)
	# print ("bruteTest -> " + str(bruteTest))
