from chessPlayer_newTree import*

def genBoard():
	newBoard = [13,11,12,15,14,12,11,13,
		    	10,10,10,10,10,10,10,10,
		    	00,00,00,00,00,00,00,00,
		    	00,00,00,00,00,00,00,00,
		    	00,00,00,00,00,00,00,00,
		    	00,00,00,00,00,00,00,00,
		    	20,20,20,20,20,20,20,20,
		    	23,21,22,25,24,22,21,23]
	return newBoard

def convertTo2D(x):
	if len(x)!=64:
		return False
	L = list(x)
	newL = []
	for i in range(0,8,1):
		tempL = []
		for j in range(0,8,1):
			#print(8*i+j)
			tempL +=[L[8*i+j]]
		newL += [tempL]
	return newL

def convertTo1D(x):
	if len(x)!=8:
		return False
	L = list(x)
	newL = []
	for i in range(0,8,1):
		tempL = []
		for j in range(0,8,1):
			#print(8*i+j)
			tempL +=[L[i][j]]
		newL += tempL
	return newL

def print2D(y):
	x = list(y)

	for i in x:
		print(i)
	return True

def printBoard(l):
	board = list(l)
	accum="---- BLACK SIDE ----\n"
	max=63
	for j in range(0,8,1):
		for i in range(max-j*8,max-j*8-8,-1):
			accum=accum+'{0: <5}'.format(board[i])
		accum=accum+"\n"
	accum=accum+"---- WHITE SIDE ----"
	return accum

def printReferenceIndex():
	print(printBoard(range(0,64,1)))
	return True

def GetPlayerPositions(board,player):#player input is 10 or 20
	if len(board)!=64:
		return False
	acc = []
	for i in range(0,64,1):
		if (int(board[i]/10) == int(player/10)):
			acc +=[i]
	return acc

def GetPieceLegalMoves(l,position):
	board = list(l)
	if (board[position]==0) or (len(board)!=64) or (position>63) or (position<0) :
		return False
	player = GetPlayer(board,position)
	piece = GetPiece(board,position)
	#print(piece)
	#print(player)
	move=[]
	if piece ==3: #for rook
		direction = [2,4,6,8]
	elif piece ==1:
		direction = [16,8,-8,-16] #special notation for knight
	elif piece == 2: #for bishop
		direction = [1,3,7,9]
	elif piece == 4: #for queen
		direction = [1,2,3,4,6,7,8,9]
	elif piece ==5: #for king
		direction = [1,2,3,4,6,7,8,9]
	elif piece ==0: #for pawn
		if player ==1:#white pawn
			direction = [1,3,2]
		else: #black pawn
			direction = [7,9,8]
	else:
		return False

	if piece ==3 or piece ==2 or piece ==4:
		for i in direction:
			incrAndBound = GetIncrementandBound(i,position)
			#print(incrAndBound)
			nextPos = position+incrAndBound[0]
			while(nextPos<=incrAndBound[2] and nextPos>=incrAndBound[1]):
				if (GetPlayer(board,nextPos)==player):
					break
				if (GetPlayer(board,nextPos)!=player) and (GetPlayer(board,nextPos)!=0):
					move +=[nextPos]
					break
				else :
					move +=[nextPos]
				nextPos+=incrAndBound[0]
				
		
	elif piece ==5:
		#print("here comes piece 5")
		for i in direction:
			incrAndBound = GetIncrementandBound(i,position)
			#print(incrAndBound)
			nextPos = position+incrAndBound[0]
			if (GetPlayer(board,nextPos)!=player) and (nextPos<=incrAndBound[2] and nextPos>=incrAndBound[1]):
				move +=[nextPos]

	elif piece ==0:
		for i in direction:
			incrAndBound = GetIncrementandBound(i,position)
			nextPos = position+incrAndBound[0]
			if (i == direction[2]) and GetPlayer(board,nextPos)==0:	
				move +=[nextPos]
			if (i == direction[0] or i == direction[1]) and ((GetPlayer(board,nextPos)!=player) and (GetPlayer(board,nextPos)!=0)) and (nextPos<=incrAndBound[2] and nextPos>=incrAndBound[1]):
				move +=[nextPos]

		
	elif piece == 1:
		for i in direction:
			if i ==16:
				if (GetPlayer(board,position+i+1)!=player) and getRow(position+i+1) == getRow(position+i) and getRow(position+i)<=7:
					move+=[position+i+1]
				if (GetPlayer(board,position+i-1)!=player) and getRow(position+i-1) == getRow(position+i) and getRow(position+i)<=7:
					move+=[position+i-1]
			elif i ==8:
				if (GetPlayer(board,position+i+2)!=player) and getRow(position+i+2) == getRow(position+i) and getRow(position+i)<=7:
					move+=[position+i+2]
				if (GetPlayer(board,position+i-2)!=player) and getRow(position+i-2) == getRow(position+i) and getRow(position+i)<=7:
					move+=[position+i-2]
			elif i ==-8:
				if (GetPlayer(board,position+i+2)!=player) and getRow(position+i+2) == getRow(position+i) and getRow(position+i)>=0:
					move+=[position+i+2]
				if (GetPlayer(board,position+i-2)!=player) and getRow(position+i-2) == getRow(position+i) and getRow(position+i)>=0:
					move+=[position+i-2]
			elif i ==-16:
				if (GetPlayer(board,position+i+1)!=player) and getRow(position+i+1) == getRow(position+i) and getRow(position+i)>=0:
					move+=[position+i+1]
				if (GetPlayer(board,position+i-1)!=player) and getRow(position+i-1) == getRow(position+i) and getRow(position+i)>=0:
					move+=[position+i-1]
			else:
				return False
	else:
			return False

	return move




def GetPlayer(board,position): #output player as 1 or 2
	if position>63 or position<0:
		#print("position out of range")
		return False
	#print("here is get player "+ str(position)+" will return "+ str(int(board[position]/10)))
	return int(board[position]/10)

def GetPiece(board,position):
	if position>63 or position<0:
		return False
	return board[position]%10

def GetIncrementandBound(direction,position): 
#return[increment,lowerB,Upperbound]
	if position>63 or position<0:
		return False
	row = getRow(position)
	col = getCol(position)

	if direction == 1:
		return [9,position,min((7-row)*9+position,(7-col)*9+position)]
	elif direction==2:
		return [8,position,(7-row)*8+position]
	elif direction==3:
		return [7,position,min((7-row)*7+position,(col)*7+position)]
	elif direction==4:
		return [1,position,(7-col)+position]
	elif direction==6:
		return [-1,position-col,position]
	elif direction==7:
		return [-7,max(row*(-7)+position,(7-col)*(-7)+position),position]
	elif direction==8:
		return [-8,row*(-8)+position,position]
	elif direction==9:
		return [-9,max(row*(-9)+position,col*(-9)+position),position]
	else:
		return False
def min(x,y):
	if x<y:
		return x
	else:
		return y
def max(x,y):
	if x>y:
		return x
	else:
		return y
def getRow(position):
	return int(position/8)

def getCol(position):
	return int(position%8)
	
def IsPositionUnderThreat(board,position,player):#player input will be 10 or 20
	if player ==10:
		opp = 20
	else:
		opp = 10
	#print(GetPlayerPositions(board,opp))
	for i in GetPlayerPositions(board,opp):
		#print("legal moves for " + str(i))
		#print(GetPieceLegalMoves(board,i))
		for j in GetPieceLegalMoves(board,i):
			if position ==j:
				return True
	return False

def ifMoveLegal(board,userMove):#userMove[2], which stores player will be 1 or 2
	if userMove[2]!=GetPlayer(board,userMove[0]):
		return False
	legalMove = GetPieceLegalMoves(board,userMove[0])
	for i in legalMove:
		if userMove[1] ==i:
			return True
	return False


def Move(board,userMove):#userMove[2], which stores player will be 1 or 2
	if ifMoveLegal(board,userMove)!= True:
		return False
	else:
		piece = GetPiece(board,userMove[0])
		board[userMove[1]] = 10*userMove[2]+piece
		board[userMove[0]] = 0
		if GetPiece(board,[userMove[1]])==0:
			if getRow(userMove[1])==7 and userMove[2]==1: #white pawn get to the end of board
				board[userMove[1]] = 14
			elif getRow(userMove[1])==0 and userMove[2]==2: #black pawn get to the end of board
				board[userMove[1]] = 24
	#print("a move is placed")
	return True
















