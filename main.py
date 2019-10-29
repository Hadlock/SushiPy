#!/usr/bin/python3

import random
import itertools
import inspect

def create52Deck():
    VALUES = "23456789TJQKA"
    SUITS = "scdh"
    return ["".join(card) for card in itertools.product(VALUES, SUITS)]
     
def createSushiDeck():
    TEMPURA = "T"  * 14
    SASHIMI = "S"  * 14
    DUMPLING = "D" * 14
    MAKI2 = "m" * 12
    MAKI3 = "M" * 8
    MAKI1 = "w" * 6
    NIGIRISAL = "N" * 10
    NIGIRISQU = "n" * 5
    NIGIRIEGG = "E" * 5
    PUDDING = "P" * 10
    WASABI = "W" * 6
    CHOPSTICKS = "C" * 0 #for now, 4 normal
    return ["".join(card) for card in itertools.chain(TEMPURA, SASHIMI, DUMPLING,
    MAKI2, MAKI3, MAKI1, NIGIRISAL, NIGIRISQU, NIGIRIEGG,
    PUDDING, WASABI, CHOPSTICKS)]

def shuffleDeck(deck):
    for i, card in enumerate(deck):
        insert_at = random.randrange(104)
        deck[i], deck[insert_at] = deck[insert_at], deck[i]

class SushiPlayer(object):
  """
    blueprint for player
  """

  def __init__(self, score, pudding, hand, passs, played):
    self.score = 0
    self.pudding = 0
    self.hand = []
    self.passs = []
    self.played = []

def dealcards(players, numplayers, deck):
    for p in range(numplayers):
        print("for p in numplayers")
        n = SushiPlayer(0,0,[],[],[])
        players.append(n)
        for r in range(8):
            card = deck.pop()
            players[p].hand.append(card)
        attrs = vars(players[p])
        print(', '.join("%s: %s" % item for item in attrs.items()))

def playround(players, deck):
    phases = len(players[0].hand)
    for p in range(phases):
        for i in range(len(players)):
            card = players[i].hand.pop()
            players[i].played.append(card)
            if card == "P":
                players[i].pudding += 1
#            for pas in players[i].hand:
#                card = players[i].hand.pop()
#                players[i].passs.append(card)
    
    for p in range(len(players)):
        attrs = vars(players[p])
        print(', '.join("%s: %s" % item for item in attrs.items()))

def game(numplayers, deck):
    players = []
    dealcards(players, numplayers, deck)
    playround(players, deck)

def main():
    print("- SushiPy!")
    deck = createSushiDeck()
    shuffleDeck(deck)
    numplayers = 4 #input("Number of Players (2-6)")
    numplayers = int(numplayers)
    game(numplayers, deck)
 
if __name__ == "__main__":
    main()