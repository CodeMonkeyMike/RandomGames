# A user only has access to their "Game Hand" after activating a "Game"
# A game will create a "Deck" and pull cards from it as needed
# The "Game Hand" will have functions applied to it from the "Game"

#Creates a deck
import hashlib
import random
import itertools

class Deck:
    def __init__(self, num_decks, user_input, system_input):
        self.ccount = 0
        self.ndecks = num_decks
        self.d = self.create_deck(num_decks, user_input, system_input)

    # Parameters number of decks, user generated input, system generated input
    def create_deck(self, num_decks, user_input, system_input):
        user_hash = int(hashlib.sha512(user_input).hexdigest(), 16)
        system_hash = int(hashlib.sha512(system_input).hexdigest(), 16)

        # XOR To create seed
        deck_seed = (user_hash ^ system_hash)

        # TODO: Dont create deck each time funcion is run
        # Constants that create a deck
        SUITS = 'cdhs'
        RANKS = '23456789TJQKA'
        DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))

        # Seed is used to create a unique but verifiable deck
        random.seed(deck_seed)

        # Mersenne Twister random generater using seed
        random_deck = random.sample(DECK, 52)

        # In place Fisher-Yates shuffle
        random.shuffle(random_deck)
        return random_deck

    # TODO: Find out if deck and card_count need to be passed to next_card
    def next_card(self):
        dealt_card = self.d[self.ccount]
        self.ccount += 1
        return dealt_card



test_deck = Deck(1, "23423432423432", "2342352345435435")
print test_deck.next_card()
print test_deck.next_card()
print test_deck.next_card()
print test_deck.d