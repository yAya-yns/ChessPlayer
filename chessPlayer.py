from chessPlayer_AI import*

def clear():
    print("\n"*100)
    return True

def chessPlayer(inputBoard,player):
	status = True
	if len(inputBoard)!=64:
		status = False
	if player!=10 and player!=20:
		status = False
	board = list(inputBoard)
	tree = levelOrderTree(genTree(board,int(player/10)))
	
	evalTree = tree
	move = improvedMove(board,int(player/10))[0:2]
	candidateMoves = getCandidateMove (board,int(player/10))

	if candidateMoves == False:
		status = False

	return[status,move,candidateMoves,evalTree]

def askForMove(player): #player input will be 1 or 2
	print("you are player " + str(10*player))
	print("By Moving the piece from A to B")
	A = input("Please enter A First: ")
	B = input("Now please enter B: ")
	return [A,B,player]

def ifEnd(board): #return false if both king alive,  return winner if one king is dead
	blackAlive = False
	whiteAlive = False
	for i in board:
		if i==25:
			blackAlive = True
		if i==15:
			whiteAlive = True
	if blackAlive==True and whiteAlive==True:
		return False #game continue
	elif blackAlive==False:
		return 1 #1 is the winner
	elif whiteAlive==False:
		return 2 #2 is the winner
	else:
		return 123

def main():
	
	board = genBoard()
	'''
	board =[13,11,12,15,14,12,11,13, #test board
			10,10,10,10,10,10,10,10,
			00,00,00,00,00,00,00,00,
			00,00,00,00,00,00,00,00,
			00,00,00,00,00,00,00,00,
			00,00,20,20,00,00,00,00,
			20,20,00,00,20,20,20,20,
			23,21,22,25,24,22,21,23]
	'''
	gameOver = False
	player = 1 #start with white player
	counter=0
	while gameOver == False:
		'''
		counter+=1
		if counter == 100:
			break
		'''
		clear()
		printReferenceIndex()
		print(printBoard(board))
		if player == 1:
			userMove = improvedMove(board,player)
			#print("for player 1")
			#print(userMove)
			#user mode#
			''' 
			legal = False
			while (legal == False):
				userMove = askForMove(player)
				if ifMoveLegal(board,userMove) == True:
					#print("move is legal")
					legal = True
				else: 
					print("Illegal Move, pleases try again")
			'''
		elif player ==2:
			userMove = randomMove(board,player)
			#print("for player 2")
			#print(userMove)
		else:
			return False
		Move(board,userMove)
		#print("a move is placed")
		if player!=1:
			player = 1
		else:
			player = 2



		gameOver = ifEnd(board) #LAST STEP. check if one of the king is dead
	print("the winner is player "+str(gameOver))
	return True
#main()
	
#for i in range(100):
#	main()
