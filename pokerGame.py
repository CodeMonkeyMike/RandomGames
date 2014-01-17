# Accepts input from pokerHand
# Initiated by the system
# Checks for winning hands

# Hands Pair, Two pair, Three of a Kind, Straight, Flush, Full House, Four of a kind, Straight Flush
import deckCreator

SUITS = ('c', 'd', 'h', 's')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
 
ORDER_LOOKUP = dict(zip(DECK, range(52)))
RANK_LOOKUP = dict(zip(RANKS, range(13)))
SUIT_LOOKUP = dict(zip(SUITS, range(4)))

class PokerGame:
	def __init__(self, num_decks, user_input, system_input):
		self.deck = deckCreator.Deck(num_decks, user_input, system_input)