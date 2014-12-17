#!/usr/bin/python

class State:
	'Handles chess board game states'
	
#	rnbkqbnr
#	pppppppp
#	xxxxxxxx
#	xxxxxxxx
#	xxxxxxxx
#	xxxxxxxx
#	PPPPPPPP
#	RNBKQBNR
	
	state = 'rnbkqbnrppppppppxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxPPPPPPPPRNBKQBNR'
	moves = []
	
	def gameOver(self):
		
	
	def toMove(self):
		return "white"
	
	def makeMove(self, move):
		
	
	def allLegalMoves(self, state):
		
	def colConversion(self, index):
		if index % 8 == 0:
			return 'a'
		elif index % 8 == 1:
			return 'b'
		elif index % 8 == 2:
			return 'c'
		elif index % 8 == 3:
			return 'd'
		elif index % 8 == 4:
			return 'e'
		elif index % 8 == 5:
			return 'f'
		elif index % 8 == 6:
			return 'g'
		elif index % 8 == 7:
			return 'h'
	
	def pawnMoves(self, state):
	
		for index, piece in enumerate(state):
			move = 'P' + colConversion(index)
			if piece == 'p' and index == 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 and state[index+8] == 'x' or 'X' and state[index+16] == 'x' or 'X':
				move += str(int(index/8)) + colConversion(index+16) + str(int((index+16)/8))
				moves.append(move)
			elif piece == 'p' and index == 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 and state[index+8] == 'x' or 'X':
				move += str(int(index/8)) + colConversion(index+8) + str(int((index+8)/8))
				moves.append(move)
				
			if index % 8 != 0 or index % 8 != 7:
				if piece == 'p' and state[index+7] != 'x' or 'X':
					move += str(int(index/8)) + colConversion(index+7) + str(int((index+7)/8))
					moves.append(move)
				elif piece == 'p' and state[index+9] != 'x' or 'X':
					move += str(int(index/8)) + colConversion(index+9) + str(int((index+9)/8))
					moves.append(move)
			elif index % 8 == 0:
				if piece == 'p' and state[index+9] != 'x' or 'X':
					move += str(int(index/8)) + colConversion(index+9) + str(int((index+9)/8))
					moves.append(move)
			elif index % 8 == 7:
				if piece == 'p' and state[index+7] != 'x' or 'X':
					move += str(int(index/8)) + colConversion(index+7) + str(int((index+7)/8))
					moves.append(move)
	
	def knightMoves(self, state):
	
		for index, piece in enumerate(state):
			move = "N" + colConversion(index)
			if index % 8 != 0 or index % 8 != 1:
				if piece == 'n' and state[index-10] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index-10) + str(int((index-10)/8))
					moves.append(move)
				elif piece == 'n' and state[index+6] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index+6) + str(int((index+6)/8))
					moves.append(move)
			elif index % 8 != 7 or index % 8 != 8:
				if piece == 'n' and state[index+10] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index+10) + str(int((index+10)/8))
					moves.append(move)
				elif piece == 'n' and state[index-6] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index-6) + str(int((index-6)/8))
					moves.append(move)
			elif int(index/8) != 1 or int(index/8) != 2:
				if piece == 'n' and state[index-17] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index-17) + str(int((index017)/8))
					moves.append(move)
				elif piece == 'n' and state[index-15] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index-15) + str(int((index-15)/8))
					moves.append(move)
			elif int(index/8) != 7 or int(index/8) != 8:
				if piece == 'n' and state[index+17] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index+17) + str(int((index+17)/8))
					moves.append(move)
				elif piece == 'n' and state[index+19] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
					move += str(int(index/8)) + colConversion(index+19) + str(int((index+19)/8))
					moves.append(move)
	
	def rookMoves(self, state):
	
		for index, piece in enumerate(state):
			move = "R" + colConversion(index)
			if state[index-1] == 'x' or 'X' or 'P' or 'R' or 'N' or 'B' or 'K' or 'Q':
				move += str(int(index/8)) + colConversion(index-1) + str(int((index-1)/8))
				moves.append(move)
			elif state[index-2]
			
	def bishopMoves(self, state):
	
		for index, piece in enumerate(state):
			move = "B" + colConversion(index)