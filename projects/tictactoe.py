def display_board(board):
	#print('\n' * 50)
	print(board[1],'|',board[2],'|',board[3])
	print(board[4],'|',board[5],'|',board[6])
	print(board[7],'|',board[8],'|',board[9])

def player_marker():
	marker=''
	while marker!='X' and marker!='O': 
		marker = input('player1 choose X or O: ').upper()

	if marker=='X':
		return ('X','O')
	
	else: 
		return ('O','X')				

def place_marker(board,player1_marker,player2_marker):
	display_board(board)
	while ' ' in board:

		i=int(input("player1 enter your position: "))
		s=space_check(board,i)
		if s:
			board[i]=player1_marker
			display_board(board)
			win=check_win(board)
			if win:
				print("Congratulations! player1 Won")
				break
		else: 
			print('invalid index')
			break
						
	
		if ' ' in board:
			i=int(input("player2 enter your position: "))
			s=space_check(board,i)
			if s:
				board[i]=player2_marker
				display_board(board)
				win=check_win(board)
				if win:
					print("Congratulations! player2 Won")
					break
			else: 
				print('invalid index')
				break		
	if ' ' not in board:
			print("Match Draw")
				
	
						
					

		
def check_win(board):
			
	if board[1]==board[2]==board[3]=='X' or board[4]==board[5]==board[6]=='X' or board[7]==board[8]==board[9]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[3]==board[6]==board[9]=='X' or board[1]==board[5]==board[9]=='X' or board[3]==board[5]==board[7]=='X':
		a=True
		
	elif board[1]==board[2]==board[3]=='O' or board[4]==board[5]==board[6]=='O' or board[7]==board[8]==board[9]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[3]==board[6]==board[9]=='O' or board[1]==board[5]==board[9]=='O' or board[3]==board[5]==board[7]=='O':
		a=True
	else: a=False	
	return a	

def space_check(board,index):
	return board[index]==' '
			



x='yes'
while x=='yes':
	board=[' ']*10
	board[0]='#'
	print('Welcome to the Game')
	player1_marker,player2_marker= player_marker()
	print('The Game begins. Good Luck!')
	place_marker(board,player1_marker,player2_marker)
	x=input("do you want to play again? enter yes or no: ")







	