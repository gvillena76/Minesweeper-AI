# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action

#REMEMBER TO KEEP TRACK OF TIME (use Chrono?)
#import time

class Square:
	#state = "UNCOVERED"
	def __init__(self,xPosition, yPosition, state, effectiveLabel, adjacentUncovered):
		self.xPosition = xPosition
		self.yPosition = yPosition
		self.state = state
		self.effectiveLabel = effectiveLabel
		self.adjacentUncovered = adjacentUncovered

class MyAI( AI ):

	#total_time_elapsed = 0.0

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		self.rowDimension = rowDimension
		self.colDimension = colDimension
		self.totalMines = totalMines
		self.lastCol = startX
		self.lastRow = startY
		self.zeroList = []
		#Starting position is always 3,1 --> uncovers 4,2 
		#self.board = [[Square("COVERED", 0, 10)]*colDimension]*rowDimension
		self.board = []
		for i in range(self.rowDimension):
			row = []
			for j in range(self.colDimension):
				row.append(Square(j+1, i+1, "COVERED", -1, -1))
			self.board.append(row)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		#time_start = time.clock()
		
		#Simple rule of thumb logic

		#EffectiveLabel(x)
		#Frontier nodes next to uncovered
		#Enumerate next steps, find inconsistencies (grows fast with n, but simpler)
		"""
		Initial Plan:
		When we uncover a tile, we give the space an effective label.
		Then check all possibilities for unmarked mines and see if it matches up with subtracting from the effective label
		We find any consistent 0's and uncover that space
		"""
		print(f"Now checking [{self.lastCol+1},{self.lastRow+1}]")
		print("Row Dimension:", self.rowDimension)

		self.board[self.lastRow][self.lastCol].state = "UNCOVERED"
		if number == 0:
			self.board[self.lastRow][self.lastCol].effectiveLabel = 0
			self.board[self.lastRow][self.lastCol].adjacentUncovered = 0

			#Top
			if self.lastRow-1 >= 0 and self.board[self.lastRow-1][self.lastCol] not in self.zeroList and self.board[self.lastRow-1][self.lastCol].state == "COVERED":
				print("Add top")
				self.board[self.lastRow-1][self.lastCol].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow-1][self.lastCol])
			
			#Bottom
			if self.lastRow+1 <= self.rowDimension-1 and self.board[self.lastRow+1][self.lastCol] not in self.zeroList and self.board[self.lastRow+1][self.lastCol].state == "COVERED":
				print("Add bottom")
				self.board[self.lastRow+1][self.lastCol].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow+1][self.lastCol])
			
			#Left
			if self.lastCol-1 >= 0 and self.board[self.lastRow][self.lastCol-1] not in self.zeroList and self.board[self.lastRow][self.lastCol-1].state == "COVERED":
				print("Add left")
				self.board[self.lastRow][self.lastCol-1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow][self.lastCol-1])
			
			#Right
			if self.lastCol+1 <= self.colDimension-1 and self.board[self.lastRow][self.lastCol+1] not in self.zeroList and self.board[self.lastRow][self.lastCol+1].state == "COVERED":
				print("Add right")
				self.board[self.lastRow][self.lastCol+1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow][self.lastCol+1])

			#top left
			if self.lastCol-1 >= 0 and self.lastRow+1 <= self.rowDimension-1 and self.board[self.lastRow+1][self.lastCol-1] not in self.zeroList and self.board[self.lastRow+1][self.lastCol-1].state == "COVERED":
				print("Add top left")
				self.board[self.lastRow+1][self.lastCol-1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow+1][self.lastCol-1])

			#top right
			if self.lastCol+1 <= self.colDimension-1 and self.lastRow + 1 <= self.rowDimension-1 and self.board[self.lastRow+1][self.lastCol+1] not in self.zeroList and self.board[self.lastRow+1][self.lastCol+1].state == "COVERED":
				print("Add top right")
				self.board[self.lastRow+1][self.lastCol+1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow+1][self.lastCol+1])

			#bottom left
			if self.lastCol-1  >= 0 and self.lastRow-1 >= 0 and self.board[self.lastRow-1][self.lastCol-1] not in self.zeroList and self.board[self.lastRow-1][self.lastCol-1].state == "COVERED":
				print("Add bottom left")
				self.board[self.lastRow-1][self.lastCol-1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow-1][self.lastCol-1])

			#bottom right
			if self.lastCol+1 <= self.colDimension-1 and self.lastRow-1 >= 0 and self.board[self.lastRow-1][self.lastCol+1] not in self.zeroList and self.board[self.lastRow-1][self.lastCol+1].state == "COVERED":
				print("Add bottom right")
				self.board[self.lastRow-1][self.lastCol+1].state = "UNCOVERED"
				self.zeroList.append(self.board[self.lastRow-1][self.lastCol+1])
				
		print("Queue:", end='')	
		for square in self.zeroList:
			print(f"[{square.xPosition}, {square.yPosition}]", end='')
		print()

		if len(self.zeroList) != 0:
			x = self.zeroList[0].xPosition - 1
			y = self.zeroList[0].yPosition - 1
			self.lastCol = x
			self.lastRow = y
			self.zeroList.pop(0)
			return Action(AI.Action.UNCOVER, x, y)

		#Focus on rules of thumb to solve!!!!

		#A good site: https://luckytoilet.wordpress.com/2012/12/23/2125/

		#Or use inference and propositional logic

		#Slightly advanced logic

		#Very advanced logic

		#Probability / Guessing
		#Get all states of mines and pick space with least number of mine states

		#time_end = time.clock()
		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
