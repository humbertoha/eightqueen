
class eightqueen:
	currentSolution = []
	solutions = []
	numQueens = 0

	def __init__(self,numeroQueens):
		self.numQueens = numeroQueens
		self.currentSolution = [0 for x in range(self.numQueens)]
		self.solutions = []
		self.placeQueen(0)

	def isSafe(self,testRow, testCol):
		if testRow == 0:
			return True
		for row in range(0, testRow):
			if testCol == self.currentSolution[row]:
				return False
			if abs(testRow - row) == abs(testCol - self.currentSolution[row]):
				return False
		return True

	def placeQueen(self,row):
		for col in range(self.numQueens):
			if not self.isSafe(row,col):
				continue
			else:
				self.currentSolution[row] = col
				if row == (self.numQueens - 1):
					self.solutions.append(self.currentSolution.copy())
				else:
					self.placeQueen(row + 1)