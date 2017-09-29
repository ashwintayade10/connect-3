import turtle as t
from minimax import minimax,play, isGameOver,printBoard
from random import randint
from alpha_beta_pruning import abpruning,play, isGameOver, printBoard


#global_board = [['-' for x in range(4)] for y in range(4)]
board = [['-' for x in range(4)] for y in range(4)]
option=-1
player='M'
flag=0

# def resetBoard():
# 	new_board = [['-' for x in range(4)] for y in range(4)]
# 	return new_board

def square(x,y):
	t.setpos(x,y)
	t.pendown()
	for i in range(4):
		t.fd(100)
		t.right(90)
	t.penup()

def green_circle(x,y):
	set_t(x,y)
	t.color('darkgreen')
	t.begin_fill()
	t.circle(49)
	t.end_fill()
	t.color('black')
	set_t(150,400)

def blue_circle(x,y):
	set_t(x,y)
	t.color('darkblue')
	t.begin_fill()
	t.circle(49)
	t.end_fill()
	t.color('black')
	set_t(150,400)


def get_row_of_move(y):
	if y>=100 and y<=200:
		return 3
	elif y>=200 and y<=300:
		return 2
	elif y>=300 and y<=400:
		return 1
	elif y>=400 and y<=500:
		return 0
	else:
		return -1

def get_col_of_move(x):
	if x>=100 and x<=200:
		return 0
	elif x>=200 and x<=300:
		return 1
	elif x>=300 and x<=400:
		return 2
	elif x>=400 and x<=500:
		return 3
	else:
		return -1

def wipe(x,y):
	set_t(x,y)
	t.color('lightblue')
	t.begin_fill()
	t.circle(49)
	t.end_fill()
	t.color('black')
	t.setpos(150,400)

def wipeBoard():
	for i in range(4):
		for j in range(4):
			wipe(150+j*100,400-i*100)

def set_t(x,y):
	t.penup()
	t.setpos(x,y)
	t.pendown()

def player_human_mini(x,y):
	i = get_row_of_move(y)
	j = get_col_of_move(x)
	if i==-1 or j==-1:
		print "Invalid"
		return
	elif i!=0 and board[i-1][j]=='-':
		print "Invalid"
		return
	elif board[i][j]!='-':
		print "Invalid"
		return
	else:
		print (i,j)
		board[i][j]='H'
		blue_circle(150+j*100,400-i*100)
		printBoard(board)
		player='M'
		res = isGameOver(board)
		if res[0]==True:
			print "Human wins"
			t.onscreenclick(None)
			#board = resetBoard()
		player_machine_mini()

def player_human_ab(x,y):
	i = get_row_of_move(y)
	j = get_col_of_move(x)
	if i==-1 or j==-1:
		print "Invalid"
		return
	elif i!=0 and board[i-1][j]=='-':
		print "Invalid"
		return
	elif board[i][j]!='-':
		print "Invalid"
		return
	else:
		print (i,j)
		board[i][j]='H'
		blue_circle(150+j*100,400-i*100)
		printBoard(board)
		player='M'
		res = isGameOver(board)
		if res[0]==True:
			print "Human wins"
			t.onscreenclick(None)
			#board = resetBoard()
		player_machine_ab()

def player_machine_mini():
	move = minimax(board)
	print move
	board[move[0]][move[1]]='M'
	printBoard(board)
	green_circle(150+move[1]*100,400-move[0]*100)
	if isGameOver(board)[0]==True:
		print "Machine wins"
		t.onscreenclick(None)
	player='H'

def player_machine_ab():
	move = abpruning(board)
	print move
	board[move[0]][move[1]]='M'
	printBoard(board)
	green_circle(150+move[1]*100,400-move[0]*100)
	if isGameOver(board)[0]==True:
		print "Machine wins"
		t.onscreenclick(None)
	player='H'

def main():				#Sets up environment
	s = t.Screen()
	s.bgcolor('lightblue')
	t.speed(0)
	t.hideturtle()
	t.tracer(0,0)
	t.setup(600,600)
	t.screensize(600, 600)
	t.setworldcoordinates(0, 0, 600, 600)

	while True:
		option = int(input("Enter Option:\n1] Show Board\n2] Play using Minimax\n3] Play using Alpha-Beta Pruning\n4] Show Results\n"))
		if option==1:
			t.penup()
			t.setpos(100,200)
			x=100
			y=200
			for i in range(4):
				for j in range(4):
					square(x,y)
					x=x+100
					t.penup()
					t.setpos(x,y)
					#set_t(x,y)
					t.penup()
				y=y+100
				x=100

		elif option==2:
			x=150
			y=400
			set_t(x,y)
			i = randint(0,3)
			board[0][i]='M'
			#global_board[0][i]='M'
			green_circle(x+i*100,y)
			player = 'H'
			t.onscreenclick(player_human_mini)

		elif option==3:
			x=150
			y=400
			set_t(x,y)
			i = randint(0,3)
			board[0][i]='M'
			#global_board[0][i]='M'
			green_circle(x+i*100,y)
			player = 'H'
			t.onscreenclick(player_human_ab)
		#else:
	t.getscreen()._root.mainloop()	


if __name__=="__main__":
	main()