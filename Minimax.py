class Minimax:
	'Minimax implementation for chess moves'

	def minimax(state, alpha, beta):
		if state.gameOver():
			return state.evaluate()
		else: 
			if state.toMove() == "white":
				bestMove = None
				for move in state.allLegalMoves():
					newState = state.makeMove(move)
					score, move = minimax(newState, alpha, beta)
					if score > alpha: 
						alpha = score
						bestMove = move
						if alpha >= beta:
							break
				return bestMove
			else:
				bestMove = None
				for move in state.allLegalMoves():
					newState = state.makeMove(move)
					score, move = minimax(newState, alpha, beta)
					if score < beta
						beta = score
						bestMove = move
						if alpha >= beta:
							break
				return bestMove