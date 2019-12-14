# A Highest Card Game, where 2 to 7 players compete against eachother
import Cards, Games

class BJ_Card(Cards.Card):
# Defines a card
	ACE_VALUE = 1
	@property
	def value(self):
		
		val = BJ_Card.CARDS.index(self.card) + 1
		if val > 10:
			val = 10

		return val
	# This object returns a number between 1 and 10,
	# representing the value of a card

class BJ_Deck(Cards.Deck):
# Defines a card deck
	def populate(self):
		for suit in BJ_Card.SUITS:
			for card in BJ_Card.CARDS:
				self.cards.append(BJ_Card(card, suit))

class BJ_Hand(Cards.Hand):
# Defines a hand
	def __init__(self, name):
		super(BJ_Hand, self).__init__()
		self.name = name
	def __str__(self):
		rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
		rep += "(" + str(self.total) + ")"
		return rep
	@property
	def total(self):

		# Add card values
		t = 0
		contains_ace = False
		for card in self.cards:
			if card.value == BJ_Card.ACE_VALUE:
				contains_ace = True
		# If the card is an Ace, add 10 to the index value of the ace card to make 11
		if contains_ace:
			
			t += 11
		else:
		    t += card.value
		return t


class BJ_Game(object):
# Defines a game
 def __init__(self, names):
  self.players = []
  for name in names:
   player = BJ_Hand(name)
   self.players.append(player)
  self.deck = BJ_Deck()
  self.deck.populate()
  self.deck.shuffle()

	
 def play(self):
  
  
  #Stores the player names and scores. These are stored in the same order
  
  names = [] 
  scores = [] 
  
  #Stores the player names who draw
  
  draw = [] 
  
  # Deal 1 card to all players
  
  self.deck.deal(self.players, per_hand = 1)
  
  #Loops through the players in the players class
  #Appends their name and score into the name and scores list in this method - These are in order
  
  for player in self.players:
   print(player)
   names.append(str(player.name))
   scores.append(player.total)
  
  #Checks to see what the maximum score is in the scores list
  #If there is only 1 item with a max score, Announces the winner
  #The winner is in the same position of the names list as scores list, so it is easy to make reference
  #If there is more then 1 item with a max score, appends each name with a max score to the draw list
  
  for x in range(0,len(scores)):
   if scores[x] == max(scores):
    if scores.count(max(scores)) == 1:
     print("\nAnd the winner is...", names[x])
    else:
     draw.append(names[x])
	 
  #If it is a draw, prints the name of the players who draw directly from the draw list
  
  if draw:
   print("It is a draw between the following players:")
   for item in draw:
    print(item)

def main():
	print("\nWelcome to the Highest Card game.\n")
	names = []
	number = Games.askForNumber("How many players? (2-7): ", low = 2, high = 8)
	print()
	i = 1
	for i in range(number):
		name = input("Enter player name: ")
		if name == "":
			names.append("Anon")
			print()
			i += 1
		else:
			names.append(name)
			print()
			i += 1
	game = BJ_Game(names)
	game.play()
main()
