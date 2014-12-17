class Minimax:
	'Minimax implementation for chess moves'

	def minimax(state, alpha, beta):
		if state.gameOver():
			return State.evaluate()
		else: 
			if State.toMove() == "white":
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					move = minimax(newState, alpha, beta)
					score = 0; #determine score?
					if score > alpha: 
						alpha = score
						bestMove = move
						if alpha >= beta:
							break
				return bestMove
			else:
				bestMove = None
				for move in State.allLegalMoves():
					newState = State.makeMove(move)
					move = minimax(newState, alpha, beta)
					score = 0; #determine score?
					if score < beta
						beta = score
						bestMove = move
						if alpha >= beta:
							break
				return bestMove