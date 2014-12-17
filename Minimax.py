class Minimax:
	'Minimax implementation for chess moves'

	def minimax(state, depth):
		if depth == 0 or state.gameOver():
			return [State.evaluate(), None]
		else: 
			if State.toMove() == "white":
				bestScore = -float(100000)
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					score, move = minimax(newState, depth - 1)
					if score > bestScore: 
						bestScore = score
						bestMove = move
				return [bestScore, bestMove]
			else:
				bestScore = float(100000)
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					score, move = minimax(newState, depth - 1)
					if score < bestScore
						bestScore = score
						bestMove = move
				return [bestScore, bestMove]