class Minimax:
	'Minimax implementation for chess moves'

	def minimax(state, depth, alpha, beta):
		if depth == 0 or state.gameOver():
			return [State.evaluate(), None]
		else: 
			if State.toMove() == "white":
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					score, move = minimax(newState, depth - 1, alpha, beta)
					if score > alpha: 
						alpha = score
						bestMove = move
						if alpha >= beta:
							break
				return [alpha, bestMove]
			else:
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					score, move = minimax(newState, alpha, beta)
					if score < beta
						beta = score
						bestMove = move
						if alpha >= beta:
							break
				return [beta, bestMove]