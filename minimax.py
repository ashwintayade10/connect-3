from random import randint



class Node:
	def __init__(self,board,player,move):
		self.board=board
		self.player=player
		self.move=move

def createNode(board,player,move):
	return Node(board,player,move)

def isGameOver(board):
	for i in range(4):
		for j in range(2):
			if board[i][j]==board[i][j+1] and board[i][j+1]==board[i][j+2] and board[i][j]!='-':
				if board[i][j]=='M':
					return (True,1)
				else:
					return (True,-1)
	for j in range(4):
		for i in range(2):
			if board[i][j]==board[i+1][j] and board[i+1][j]==board[i+2][j] and board[i][j]!='-':
				if board[i][j]=='M':
					return (True,1)
				else:
					return (True,-1)

	if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!='-':
		if board[0][0]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[1][1]==board[2][2] and board[2][2]==board[3][3] and board[1][1]!='-':
		if board[1][1]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[1][0]==board[2][1] and board[2][1]==board[3][2] and board[1][0]!='-':
		if board[1][0]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[0][1]==board[1][2] and board[1][2]==board[2][3] and board[0][1]!='-':
		if board[0][1]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!='-':
		if board[0][2]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[1][3]==board[2][2] and board[2][2]==board[3][1] and board[1][3]!='-':
		if board[1][3]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[0][3]==board[1][2] and board[1][2]==board[2][1] and board[0][3]!='-':
		if board[0][3]=='M':
			return (True,1)
		else:
			return (True,-1)
	if board[1][2]==board[2][1] and board[2][1]==board[3][0] and board[1][2]!='-':
		if board[1][2]=='M':
			return (True,1)
		else:
			return (True,-1)

	flag=0
	for i in range(4):
		for j in range(4):
			if board[i][j]=='-':
				flag=1
	if flag==0:
		return (True,0)		
	return (False,0)


def getMoves(board):
	moves=[]
	for j in range(4):
		for i in range(4):
			if board[i][j]=='-':
				moves.append((i,j))
				break
	#print moves
	return moves

def getChildren(board,player):
	moves=getMoves(board)
	children=[]
	for m in moves:
		new_board = [['-' for x in range(4)] for y in range(4)]
		for i in range(4):
			for j in range(4):
				new_board[i][j]=board[i][j]
		new_board[m[0]][m[1]]=player
		children.append(createNode(new_board,player,m))
	return children

# def minimax(board,player):
# 	move = (-1,-1)
# 	res= isGameOver(board,player)
# 	if res[0]==True:
# 		return (res[1],move)
# 	if player=='M':
# 		best_val = float("-inf")
# 		children = getChildren(board,'M')
# 		for c in children:
# 			(v,temp) = minimax(c.board,'H')
# 			best_val = max(best_val,v)
# 			if best_val==v:
# 				move = c.move
# 		return (best_val,move)
# 	else:
# 		best_val=float("inf")
# 		children = getChildren(board,'H')
# 		for c in children:
# 			(v,temp) = minimax(c.board,'M')
# 			best_val = min(best_val,v)
# 			if best_val==v:
# 				move = c.move
# 		return (best_val,move)

def minimax(board):
	actions = getChildren(board,'M')
	max_a = -2
	move_a = (-1,-1)
	#printBoard(board)
	#print "\n"
	for a in actions:
		v = minValue(a.board)
		if v>max_a:
			max_a = v
			move_a = a.move
	return move_a

def maxValue(board):
	#printBoard(board)
	#print "\n"
	res = isGameOver(board)
	if res[0]==True:
		return res[1]
	v = -2
	actions = getChildren(board,'M')
	for a in actions:
		t = minValue(a.board)
		if t>v:
			v = t
	return v

def minValue(board):
	#printBoard(board)
	#print "\n"
	res = isGameOver(board)
	if res[0]==True:
		return res[1]
	v = 2
	actions = getChildren(board,'H')
	for a in actions:
		t = maxValue(a.board)
		if t<v:
			v = t
	return v 


def printBoard(board):
	for i in range(4):
		for j in range(4):
			print board[i][j],
		print

def play(board,HCol):
	new_board = [['-' for x in range(4)] for y in range(4)]
	for i in range(4):
		for j in range(4):
			new_board[i][j]=board[i][j]
	for i in range(4):
		if new_board[i][HCol]=='-':
			new_board[i][HCol]='H'
			return new_board

def main():
	#str1 = "-MHM--H---------"
	#str1 = "HMHMMHHM--MH----"
	str1 = "----------------"
	board = [['-' for x in range(4)] for y in range(4)]
	# k=0
	# for i in range(4):
	# 	for j in range(4):
	# 		board[i][j]=str1[k]
	# 		k=k+1
	# res = isGameOver(board)
	# print res

	# move = minimax(board)
	# printBoard(board)
	# print move

	i = randint(0,3)
	board[0][i]='M'
	player = 'H'
	printBoard(board)
	while True:
		HCol = int(input("Enter coloumn number: "))
		board = play(board,HCol)
		printBoard(board)
		if isGameOver(board)[0]==True:
			print "Human Wins"
			break
		player='M'
		move=minimax(board)
		print move
		board[move[0]][move[1]]='M'
		printBoard(board)
		if isGameOver(board)[0]==True:
			print "Machine Wins"
			break
		player='H'

if __name__=="__main__":
	main()