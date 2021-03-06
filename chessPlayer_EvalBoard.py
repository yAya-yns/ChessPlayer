from chessPlayer_Board import*	

def getEvalTable(inputBoard,position):
	if position>63 or position<0 or len(inputBoard)!=64:
		return False
	board = list(inputBoard)
	player = GetPlayer(board,position) #player = 1 or 2
	piece = GetPiece(board,position)
	#print(player)
	#print(piece)
	if player == 2: #black 
		if piece ==0:
			EvalTable = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        				 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        				 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        				 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        				 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        				 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
        				 0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
        				 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

		elif piece ==1:
			EvalTable = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        				 -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        				 -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        				 -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        				 -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        				 -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        				 -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        				 -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]	
		elif piece ==2:
			EvalTable = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
    					  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
    					  -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
    					  -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
    					  -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
    					  -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
    					  -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
		elif piece ==3:
			EvalTable = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
    					   0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					   0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
		elif piece ==4:
			EvalTable = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
    					  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
    					  -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
    					   0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
    					  -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
		elif piece ==5:
			EvalTable = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
    					  -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
    					   2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
    					   2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
		else:
			return False
		
		
	elif player ==1: #white
		if piece ==0:
			TempTable = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        				 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        				 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        				 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        				 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        				 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
        				 0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
        				 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
			EvalTable = reverseArray(TempTable)
		elif piece ==1:
			TempTable = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        				 -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        				 -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        				 -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        				 -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        				 -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        				 -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        				 -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
			EvalTable = reverseArray(TempTable)
		elif piece ==2:
			TempTable = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
    					  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
    					  -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
    					  -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
    					  -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
    					  -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
    					  -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
			EvalTable = reverseArray(TempTable)

		elif piece ==3:
			TempTable = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
    					   0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
    					   0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
			EvalTable = reverseArray(TempTable)
		elif piece ==4:
			TempTable = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
    					  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
    					  -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
    					   0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
    					  -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
    					  -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
    					  -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
			EvalTable = reverseArray(TempTable)
		elif piece ==5:
			TempTable = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
    					  -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
    					  -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
    					   2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
    					   2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
			EvalTable = reverseArray(TempTable)
		else:
			return False
		
	else:
		return False


	return EvalTable

def reverseArray(array):
	newArray = []
	for i in range(0,len(array),1):
		newArray =[array[i]] +newArray
	return newArray

def evalBoard(inputBoard):
	if len(inputBoard)!=64:
		return False
	board = list(inputBoard)
	score = 0.0
	for i in range(0,64,1):
		score+=evalPosition(board,i)
	return float(score)

def evalPosition(inputBoard,position): #return a float
	if position>63 or position<0 or len(inputBoard)!=64:
		return False
	board = list(inputBoard)
	if board[position] == 0:
		return 0.0
	Eval = 0.0
	placeValue = 10*getEvalTable(board,position)[position]
	Eval = placeValue+getPieceValue(board,position)
	return float(Eval)

def getPieceValue(inputBoard,position):
	if position>63 or position<0 or len(inputBoard)!=64:
		return False
	board = list(inputBoard)
	player = GetPlayer(board,position) #player = 1 or 2
	piece = GetPiece(board,position)
	if board[position] == 0:
		return 0.0
	if player ==1:
		s = 1
	elif player ==2:
		s = -1
	else:
		return False
	if piece ==0:
		val = 10
	elif piece ==1:
		val = 30
	elif piece ==2:
		val = 30
	elif piece ==3:
		val = 50
	elif piece ==4:
		val = 90
	elif piece ==5:
		val = 900
	else:
		return False
	return float(s*val)

