INFINITY = 100000

def minimax(state, depth):
	if depth == 0 or state.isCheckmate() or state.isDraw():
		return state.evaluate()
	else: 
		if state.toMove() == "white":
			bestScore = -float(INFINITY)
			bestMove = None
			for move in state.allLegalMoves():
				newState = state.makeMove(move)
				score, move = minimax(newState, depth - 1)
				if score > bestScore: 
					bestScore = score
					bestMove = move
			return bestMove
		else:
			bestScore = float(INFINITY)
			bestMove = None
			for move in state.allLegalMoves():
				newState = state.makeMove(move)
				score, move = minimax(newState, depth - 1)
				if score < bestScore
					bestScore = score
					bestMove = move
			return bestMove