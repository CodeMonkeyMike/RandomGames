import itertools
import deckCreator

SUITS = ('c', 'd', 'h', 's')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

RANK_LOOKUP = dict(zip(RANKS, range(13)))
SUIT_LOOKUP = dict(zip(SUITS, range(4)))

def merge_sort(li):
  if len(li) < 2: return li
  m = len(li) / 2
  return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
  result = []
  i = j = 0
  while i < len(l) and j < len(r):
    if rank_num(l[i]) < rank_num(r[j]):
      result.append(l[i])
      i += 1
    else:
      result.append(r[j])
      j += 1
  result += l[i:]
  result += r[j:]
  return result

def rank(card):
	return card[0]

def rank_num(card):
	return RANK_LOOKUP[card[0]]

def suit(card):
	return card[1]

def suit_num(card):
	return SUIT_LOOKUP[card[1]]

def flush(hand):
	s = suit(hand[0])
	return all(suit(card) == s for card in hand)

def pair(hand):
	c = 0
	p = rank_num(hand[0])
	a = []
	for card in hand:
		sn = rank_num(card)
		print c
		if sn == p:
			c += 1
		else:
			if c > 1:
				a.append([c,p])
			c = 1
			p = sn
	if c > 1:
		a.append([c,p])
	return a

def strait(hand):
	t = 0
	return [t += rank_num(card) for card in hand]

my_deck = deckCreator.Deck(124,"12312","124312")

print my_deck.d

hand = []
hand.append(my_deck.next_card())
hand.append(my_deck.next_card())
hand.append(my_deck.next_card())
hand.append(my_deck.next_card())
hand.append(my_deck.next_card())

print hand
print merge_sort(hand)
print pair(hand)
print strait(hand)
# def check_hand(hand):


# def strait(hand):
# 	h = rank_num(hand[0])
# 	for card in hand:
# 		cur = rank_num(card)
# 		rank_total += cur
# 		if cur > h:
# 			h = cur
# 	return h * 5 - 10 == rank_total
# def pair(hand):

# Fush, Strait, Royal
# Fush, Not Strait, Pairs