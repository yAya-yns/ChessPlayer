from chessPlayer_EvalBoard import*
import random

def optimization(L):
	l = list(L)
	newL=[]
	for i in range(0,4,1):
		random.shuffle(l)
		newL+=l
	return newL


def allSafeMoves(board,player):#player input will be 1 or 2
	acc = []
	if len(board)!=64:
		return False
	currentPos = GetPlayerPositions(board,player*10)
	for i in currentPos:
		for j in GetPieceLegalMoves(board,i):
			if IsPositionUnderThreat(board,j,player*10)==False:
				acc+=[[i,j]]
	return acc

def randomMove(board,player): #player input will be 1 or 2.  return a 3-list
	possibleMove = allSafeMoves(board,player)
	if len(possibleMove)==1:
		Move = possibleMove[0]
	elif len(possibleMove)==0:
		Move = [False,False]
	else:
		Move = possibleMove[random.randint(0,len(possibleMove)-1)]
	Move+=[player]
	return Move


def genTree(inputBoard,player):
	tree = [inputBoard,player]
	return tree

def improvedMove(board,player):
	possibleMove = allSafeMoves(board,player)
	if len(possibleMove)==1:
		BestMove = possibleMove[0]
		BestMove+=[player]
	elif len(possibleMove)==0:
		BestMove = [False,False]
		BestMove+=[player]
	else:
		scoreBoard = []
		for i in possibleMove:
			i+=[player]
			tempBoard = list(board)
			a = Move(tempBoard,i)
			scoreBoard+=[evalBoard(tempBoard)]
		bestMoveIndex = 0
		if player ==1:
			score = -9999999
			for j in range(0,len(scoreBoard)-1,1):
				if scoreBoard[j]> score:
					score =scoreBoard[j]
					bestMoveIndex = j
		elif player == 2:
			score = 9999999
			for j in range(0,len(scoreBoard)-1,1):
				if scoreBoard[j]< score:
					score =scoreBoard[j]
					bestMoveIndex = j
		else:
			return False
		BestMove = possibleMove[bestMoveIndex]
	
	return BestMove

def getScoreofAMove(board,move):#player is 1 or 2
	score = 0.0
	player = GetPlayer(board,move[0])
	tempBoard = list(board)
	move+=[player]
	a = Move(tempBoard,move)
	score = evalBoard(tempBoard)
	return float(score)

def levelOrderTree(tree):
	board = list(tree[0])
	player = tree[1]
	L = []
	for i in range(0,len(getCandidateMove(board,player)),1):
		L+=[getCandidateMove(board,player)[i][1]]

	L = optimization(L)


	return L





def getCandidateMove (board,player):
	possibleMove = allSafeMoves(board,player)
	CandidateMove = []
	tempBoard = list(board)
	if len(possibleMove)==1:
		CandidateMove = [possibleMove[0],getScoreofAMove(tempBoard,possibleMove[0])]
	elif len(possibleMove)==0:
		return False
	else:
		for i in possibleMove:
			CandidateMove += [[possibleMove[0],getScoreofAMove(tempBoard,i)]]
	
	return CandidateMove




