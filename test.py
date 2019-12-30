from chessPlayer import*

def main():
	testBoard =[13,11,12,15,14,12,11,13,
				10,10,10,10,10,10,10,10,
				00,00,00,00,00,00,00,00,
				00,11,00,00,00,00,00,00,
				00,00,00,00,13,00,00,00,
				00,00,00,00,00,00,00,00,
				20,00,10,00,20,20,20,20,
				23,00,00,00,24,22,21,23]
	print (printBoard(range(0,64,1)))	
	print(printBoard(genBoard()))
	#print(chessPlayer(genBoard(),10))

	
	for i in range(100):
		j = (chessPlayer(testBoard,20))
		print(j)

		

	


	'''
	x=GetPieceLegalMoves(testBoard,25)
	print(x)
	for i in x:
		print(IsPositionUnderThreat(testBoard,i,10))
	print(allSafeMoves(testBoard,1))
	'''

	
main()