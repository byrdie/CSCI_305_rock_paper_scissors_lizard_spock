# Roy Smart
# Rock, Paper, Scissors, Lizard, Spock
# Lab 2
# CSCI 305 Concepts of Programming languages
# Yay first program in Python!

from enum import Enum
import random
from random import SystemRandom

# Global variables for last move bot
last_elem_1 = 0
last_elem_2 = 0

# Enumeration for battle elements
class Elem(Enum):
	rock = 0
	paper = 1
	scissors = 2	
	spock  = 3
	lizard = 4

# Enumeration for the result of the game
class Result(Enum):
	lose = -1
	tie = 0
	win = 1

# Enumeration for storing the possible players
class Play(Enum):
	HumanNotBot = 1
	StupidBot = 2
	RandomBot = 3
	IterativeBot = 4
	LastPlayBot = 5
	MyBot = 6	

# Superclass for each of the elements of the game: rock, paper, scissors, lizard, spock
class Element:

	# Constructor for objects of type Element (Not sure why this is here, it would be more 
	# efficient for each subclass to have its own constructor)
	def __init__(self, name):
		self._name = name

	# Getter method for element name
	def name(self):
		return self._name

	# Comparison method that will be overridden in each subclass
	def compareTo(self):
		raise NotImplementedError("Not yet implemented")

	# Functions to return strings for python function dictionary lookup
	def rock_rock():
		return "Rock equals Rock"
	def rock_lizard():
		return "Rock crushes Lizard"
	def rock_scissors():
		return "Rock crushes Scissors"
	def paper_paper():
		return "Paper equals Paper"
	def paper_rock():
		return "Paper covers Rock"
	def paper_spock():
		return "Paper disproves Spock"
	def scissors_scissors():
		return "Scissors equals Scissors"
	def scissors_paper():
		return "Scissors cut Paper"
	def scissors_lizard():
		return "Scissors decapitate Lizard"
	def spock_spock():
		return "Spock equals Spock"
	def spock_scissors():
		return "Spock smashes Scissors"
	def spock_rock():
		return "Spock vaporizes Rock"
	def lizard_lizard():
		return "Lizard equals Lizard"
	def lizard_spock():
		return "Lizard poisons Spock"
	def lizard_paper():
		return "Lizard eats Paper"

	# Decision tree for winning / losing
	def decision(val, zero, one, two, three, four):
		if val == zero:
			result = Result.tie
		elif val == one or val == two:
			result = Result.win
		elif val == three or val == four:
			result = Result.lose
		else:
			print("Not in enumeration!")

		return result;

# Subclass for rock element
class Rock(Element):

	# Override compareTo method in superclass
	def compareTo(self, other):		

		# Dictionary lookup for comparisons against rock
		options = {
			Elem.rock : Element.rock_rock,
			Elem.paper : Element.paper_rock,
			Elem.scissors : Element.rock_scissors,
			Elem.spock : Element.spock_rock,
			Elem.lizard : Element.rock_lizard,
		}
		
		# Enumeration value for comparison element
		val = other.name()

		# Compute return string using dictionary
		return_str = options[val]()

		# Compute win or loss
		result = Element.decision(val, Elem.rock, Elem.scissors, Elem.lizard, Elem.paper, Elem.spock)

		return [return_str, result]

# Subclass for paper element
class Paper(Element):

	# Override compareTo method in superclass
	def compareTo(self, other):		

		# Dictionary lookup for comparisons against rock
		options = {
			Elem.paper : Element.paper_paper,
			Elem.scissors : Element.scissors_paper,
			Elem.spock : Element.paper_spock,
			Elem.lizard : Element.lizard_paper,
			Elem.rock : Element.paper_rock,
		}
		
		# Enumeration value for comparison element
		val = other.name()

		# Compute return string using dictionary
		return_str = options[val]()

		# Compute win or loss
		result = Element.decision(val, Elem.paper, Elem.rock, Elem.spock, Elem.scissors, Elem.lizard)

		return [return_str, result]

# Subclass for scissor element
class Scissors(Element):

	# Override compareTo method in superclass
	def compareTo(self, other):		

		# Dictionary lookup for comparisons against rock
		options = {			
			Elem.scissors : Element.scissors_scissors,
			Elem.spock : Element.spock_scissors,
			Elem.lizard : Element.scissors_lizard,
			Elem.rock : Element.rock_scissors,
			Elem.paper : Element.scissors_paper,
		}
		
		# Enumeration value for comparison element
		val = other.name()

		# Compute return string using dictionary
		return_str = options[val]()

		# Compute win or loss
		result = Element.decision(val, Elem.scissors, Elem.paper, Elem.lizard, Elem.rock, Elem.spock)

		return [return_str, result]

# Subclass for spock element
class Spock(Element):

	# Override compareTo method in superclass
	def compareTo(self, other):		

		# Dictionary lookup for comparisons against rock
		options = {			
			Elem.spock : Element.spock_spock,
			Elem.lizard : Element.lizard_spock,
			Elem.rock : Element.spock_rock,
			Elem.paper : Element.paper_spock,
			Elem.scissors : Element.spock_scissors,
		}
		
		# Enumeration value for comparison element
		val = other.name()

		# Compute return string using dictionary
		return_str = options[val]()

		# Compute win or loss
		result = Element.decision(val, Elem.spock, Elem.scissors, Elem.rock, Elem.lizard, Elem.paper)

		return [return_str, result]

# Subclass for lizard element
class Lizard(Element):

	# Override compareTo method in superclass
	def compareTo(self, other):		

		# Dictionary lookup for comparisons against rock
		options = {						
			Elem.lizard : Element.lizard_lizard,
			Elem.rock : Element.rock_lizard,
			Elem.paper : Element.lizard_paper,
			Elem.scissors : Element.scissors_lizard,
			Elem.spock : Element.lizard_spock,
		}
		
		# Enumeration value for comparison element
		val = other.name()

		# Compute return string using dictionary
		return_str = options[val]()

		# Compute win or loss
		result = Element.decision(val, Elem.lizard, Elem.paper, Elem.spock, Elem.scissors, Elem.rock)

		return [return_str, result]

# Superclass for players
class Player():

	# Constructor
	def __init__(self, name, player):
		self._name = name
		self._player = player

	# Getter method for player name
	def name(self):
		return self._name

	# Comparison method that will be overridden in each subclass
	def play(self):
		raise NotImplementedError("Not yet implemented")

	# Methods for initializing each element
	def init_rock():
		return Rock(Elem.rock)
	def init_paper():
		return Paper(Elem.paper)
	def init_scissors():
		return Scissors(Elem.scissors)
	def init_spock():
		return Spock(Elem.spock)
	def init_lizard():
		return Lizard(Elem.lizard)

	# Dictionary for accessing initialization methods
	elements = {
		Elem.rock : init_rock,
		Elem.paper : init_paper,
		Elem.scissors : init_scissors,
		Elem.spock : init_spock,
		Elem.lizard : init_lizard,
	}

# Subclass for stupid bot
class Stupid_bot(Player):

	# return the same move each time
	def play(self):
		return Player.elements[Elem.rock]()

# Subclass for random bot
class Random_bot(Player):

	# return random move each time
	def play(self):
		choice = random.choice(list(Elem))
		return Player.elements[choice]()

# subclass for iterative bot
class Iterative_bot(Player):

	elem_list = list(Elem)	# convert enumeration to list
	i = -1;	# index to keep track of element iteration

	# Iterate different move each play
	def play(self):
		self.i = (self.i + 1) % 5		# 5 possible elements
		return Player.elements[self.elem_list[self.i]]()

# Subclass for Last Play Bot
class Last_play_bot(Player):

	# Play the move the opponent used last round
	def play(self):

		# Use global variables to track last move
		global last_elem_1
		global last_elem_2		

		if self._player == 1 and last_elem_2 != 0:
			return last_elem_2
		elif self._player == 2 and last_elem_1 != 0:
			return last_elem_1
		else:
			return Player.elements[Elem.rock]()

# Subclass for Human input
class Human(Player):

	# Play the move the user picks
	def play(self):
		
		# Print list of possible moves
		for name, member in Elem.__members__.items():
			print(member.value + 1, ":", name) 

		# Loop untl we get appropriate input
		choice = 0
		while True:
			choice = int(input("Enter next move: "))

			if choice > 0  and choice < 6:
				break 
			else:
				print("Invalid move, please try again")

		return Player.elements[Elem(choice - 1)]()	# offset for zero based indices

# Class to store instance of custom bot
class My_bot(Player):

	# Cryptographically secure RNG
	cryptogen = SystemRandom()

	# Pit the system random number generator aginst the Python pseudo-random number generator
	# Apologies if this does not work on your system
	def play(self):

		# Generate new random number
		crypt = self.cryptogen.randrange(5)

		return self.elements[Elem(crypt)]()


# Not sure why we're implementing a main class. Classes should not be created for only one instance
class Main():

	# dictionary for possible players
	players = {
		Play.HumanNotBot : Human,
		Play.StupidBot : Stupid_bot,
		Play.RandomBot : Random_bot,
		Play.IterativeBot : Iterative_bot,
		Play.LastPlayBot : Last_play_bot,
		Play.MyBot : My_bot
	}

	# Main method
	def main():

		# results = [[0 for x in range(cols)] for x in range(rows)]
		results = {}

		# Variables for keeping track of match results
		player_1_wins = 0
		player_2_wins = 0

		# Global variables to help out last play bot
		global last_elem_1
		global last_elem_2

		print("Welcome to Rock, Paper, Scissors, Lizard Spock!") 
		print("Developed by Roy Smart\n")
		print("Please pick two players by entering the corresponding number") 
		max_player = Main.print_players()
		print()

		print("Select Player 1:") 
		choice = Play(Main.get_player())
		player_1 = Main.players[choice](choice, 1)

		print("Select Player 2:")
		choice = Play(Main.get_player())
		player_2 = Main.players[choice](choice, 2)

		print(player_1.name().name + " vs. " + player_2.name().name + " for five rounds\n")

		results[0] = ["", "Player 1", player_1.name().name, "", "Player 2", player_2.name().name, ""]
		results[1] = ["Round", "Choice", "Result",	"", "Choice", "Result", "As told by Sheldon:\n"]

		# loop through five rounds
		for i in range (0, 5):
			
			# Execute play method for both participants
			elem_1 = player_1.play()
			elem_2 = player_2.play()

			# Update the last move fields for LastPlayBot	
			last_elem_1 = elem_1
			last_elem_2 = elem_2

			res = elem_1.compareTo(elem_2)	# Compare the plays of the two bots
			
			# Decide who won or lost
			player_1_res = ""
			player_2_res = ""
			total_res = ""
			if res[1] == Result.tie:	#tie
				player_1_res = player_2_res = "tie"
				total_res = "The round was a tie"
			elif res[1] == Result.win: # win
				player_1_res = "win"
				player_2_res = "loss"
				total_res = "Player 1 won the round"
				player_1_wins += 1
			elif res[1] == Result.lose: # loss
				player_2_res = "win"
				player_1_res = "loss"
				total_res = "Player 2 won the round"
				player_2_wins += 1

			# Store output in result array
			# results[i + 2] = ["", "", player_1_res, "", "", player_2_res, res[0]]
			results[i + 2] = [str(i + 1), elem_1.name().name, player_1_res, "", elem_2.name().name, player_2_res, res[0]]

			# If a human is playing, print additional output
			if player_1.name() == Play.HumanNotBot or player_2.name() == Play.HumanNotBot:
				print("Round ", i, ":")
				print("     Player 1 chose", elem_1.name().name)
				print("     Player 2 chose", elem_2.name().name)
				print("    ", res[0])
				print("    ", total_res)
				print()
			
			
		# Print column-formatted output
		for row in results:
			print("{: <10} {: <10} {: <11} {: <10} {: <10} {: <15} {: <20}".format(*results[row]))

		# Print the score and the winner
		print("The score is ", player_1_wins, "to", player_2_wins)

		if player_1_wins > player_2_wins:
			print("Player 1 won the game!")
		elif player_2_wins > player_1_wins:
			print("Player 2 won the game!")
		else:
			print("The game was a draw")

	# Prints out list of players
	def print_players():
		for name, member in Play.__members__.items():
			print(member.value, ":", name)

	# Gets the user's input on which player to choose
	def get_player():		
		# Loop untl we get appropriate input
		choice = 0
		while True:
			choice = int(input())

			if choice > 0  and choice < 7:
				return choice 
			else:
				print("Invalid player, please try again")



# Program entry point
Main.main()






