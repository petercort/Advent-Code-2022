## List of characters, 
## split in half, first half is compartment 1, second half is compartment 2



#inventory = "vJrwpWtwJgWrhcsFMMfFFhFp"

def splitInventory(inventory, splitSize):
	bagOne = inventory[:len(inventory)//splitSize]
	bagTwo = inventory[len(inventory)//splitSize:]
	return [bagOne, bagTwo]

def identifyDups(bagOne, bagTwo):


#splitInventory(inventory)

def testSplit():
	assert splitInventory("vJrwpWtwJgWrhcsFMMfFFhFp", 2) == ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]
	assert splitInventory("vJrwpWtwJgWrhcsFMMfFFhFp", 4) == ["vJrwpW", "twJgWr", "hcsFMM", "fFFhFp"]




if __name__ == "__main__":
	testSplit()
	print("Passed")