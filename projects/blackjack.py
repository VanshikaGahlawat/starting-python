#GLOBAL VARIABLES
import random
playing=True
suits=('hearts','diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

#CLASSES
#card class (description of a card)
class Cards():
	"""docstring for Cards"""
	def __init__(self,suit,rank):
	
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank+' of '+self.suit

#deck class (deck of 52 cards)
class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Cards(suit,rank))

	def __str__(self):
		deck_comp=''
		for card in self.deck:
			deck_comp+='\n'+ card.__str__()
		return 'the deck has following cards: '+deck_comp	

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card=self.deck.pop()
		return single_card

#hand class (player and dealer's hand)
class Hand():
	"""docstring for Hand"""
	def __init__(self):
		self.cards= []
		self.value=0
		self.aces=0

	def add_cards(self,card):
		self.cards.append(card)
		self.value+=values[card.rank]

		if card.rank=='ace':
			self.aces+=1

	def adjust_ace(self):
		while self.value>21 and self.aces>0:
			self.value-=10
			self.aces-=1

#chip class (total avail chips and placed bet)
class Chip():
	def __init__(self,total=100):
		self.total=total
		self.bet=0

	def win_bet(self):
		self.total+=self.bet

	def lose_bet(self):
		self.total-=self.bet


#FUNCTIONS
#input bet 
def take_bet(chips):
	while True:	
		try: chips.bet=int(input('enter the amount you want to bet: '))
		except:
			print('enter a value')
		else:
			if chips.bet>chips.total:
				print("you don't have enough chips")	
			else:
				break	

#when player chooses hit
def hit(deck,hand):
	single_card=deck.deal()
	hand.add_cards(single_card)
	hand.adjust_ace()

#choose hit or stand
def hit_or_stand(deck,hand):
	global playing
	while True:
		x=input('Hit or Stand? enter h or s: ')
		if x.lower()=='h':
			hit(deck,hand)
		elif x.lower()=='s':
			print('player stands')
			playing=False
		else:
			print('enter correct choice')
			continue
		break		
#win or bust functions:
def player_busts(player,dealer,chips):
	print('player busts')
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print('player wins')
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print('dealer busts')
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print('dealer wins')
	chips.lose_bet()
#when a tie
def push(player,dealer):
	print('its a tie')	

#display partial cards of dealer and all cards of player
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ') # * is upackaging operator(shows all contents of the list) and sep stands for separator

#display all cards of dealer and player    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


#FINALL PROGRAM RUN
while True:
	print('hey! welcome to blackjack!\nhere ace can have values 11 and 1')

	#create deck and shuffle it
	deck=Deck()
	deck.shuffle()

	#assign 2 cards to player and dealer
	player_hand=Hand()
	player_hand.add_cards(deck.deal())
	player_hand.add_cards(deck.deal())

	dealer_hand=Hand()
	dealer_hand.add_cards(deck.deal())
	dealer_hand.add_cards(deck.deal())

	#ask player to place bet
	player_chips=Chip()
	take_bet(player_chips)

	show_some(player_hand,dealer_hand)

	#game begins
	while playing:
		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)

		if player_hand.value>21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	#player hits stand		
	if player_hand.value<=21:
		while dealer_hand.value<17:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value>21:
			dealer_busts(player_hand,dealer_hand,player_chips)	
		elif dealer_hand.value>player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value<player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else: push(player_hand,dealer_hand)

	#print the final chips with the player
	print('players winnings stand at: ',player_chips.total)	
		
	#play again?
	new_game=input('do you want to play again? enter y or n:')
	if new_game=='y':
		playing=True
		continue
	else: 
		print('thanks for playing')
		break	

#END OF PROGRAM								










