#!/usr/bin/python3

import random
import itertools
import inspect
from collections import Counter
     
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

  def __init__(self, score, makiscore, pudding, hand, passs, played):
    self.score = 0
    self.makiscore = 0
    self.pudding = 0
    self.hand = []
    self.passs = []
    self.played = []

def dealcards(players, numplayers, deck):
    for p in range(numplayers):
        print("for p in numplayers")
        n = SushiPlayer(0,0,0,[],[],[])
        players.append(n)
        for r in range(8):
            card = deck.pop()
            players[p].hand.append(card)
        attrs = vars(players[p])
        print(', '.join("%s: %s" % item for item in attrs.items()))

def passcards(players):
    for p in range(len(players)):
        for c in range(len(players[p].passs)):
            card = players[p].passs.pop()
            print(p)
            players[p].hand.append(card)
            attrs = vars(players[p])
            print(', '.join("%s: %s" % item for item in attrs.items()))


def playround(players, deck):
    phases = len(players[0].hand)
    for p in range(phases):
    # for each phase
        for i in range(len(players)):
        # for each player

            # if there are passed cards, put them in your hand
            if len(players[i].passs) > 0:
                for pas in players[i].passs:
                    card = players[i].passs.pop()
                    players[i].hand.append(card)

            # play a card
            card = players[i].hand.pop()
            players[i].played.append(card)
            
            # if the card is pudding, count it
            if card == "P":
                players[i].pudding += 1

            # prepare all remaining cards to be passed
            for pas in range(len(players[i].hand)):
                card = players[i].hand.pop()
                players[i].passs.append(card)

            # pass cards to next player
            passcards(players)
    
    for p in range(len(players)):
        attrs = vars(players[p])
        print(', '.join("%s: %s" % item for item in attrs.items()))

def scoredumplings(rawscore):
    if rawscore["D"] == 5:
        return 15
    if rawscore["D"] == 4:
        return 10
    if rawscore["D"] == 3:
        return 6
    if rawscore["D"] == 2:
        return 3
    if rawscore["D"] == 1:
        return 1
    return 0

def scorenigiri(rawscore):
    salmon = rawscore["N"] * 2
    squid = rawscore["n"] * 3
    egg = rawscore["E"] * 1
    return (salmon + squid + egg)

def scoretempura(rawscore):
    return ( (rawscore["T"]//2) * 5 )

def scoresashimi(rawscore):
    return ( (rawscore["S"]//3) * 10 )

def scoremaki(rawscore):
    return( (rawscore["M"] * 3) + (rawscore["m"] * 2) + (rawscore["w"] * 1) )

def scoreround(players):
    makiscore = []
    for p in range(len(players)):
        rawscore = Counter(players[p].played)
        print(rawscore)
        players[p].score += scoredumplings(rawscore)
        players[p].score += scorenigiri(rawscore)
        players[p].score += scoretempura(rawscore)
        players[p].makiscore += scoremaki(rawscore)

        makiscore.append(players[p].makiscore)
    
    m = max(makiscore)
    makiwinners = []
    makiwinners.append([i for i, j in enumerate(makiscore) if j == m])
    print(makiwinners)
    if len(makiscore) == 1:
        players[makiscore].score += 6    


def finalscore(players):
    for p in range(len(players)):
        print(players[p].score)

def game(numplayers, deck):
    players = []
    dealcards(players, numplayers, deck)
    playround(players, deck)
    scoreround(players)
    print("Final Scores: ")
    finalscore(players)

def main():
    print("- SushiPy!")
    deck = createSushiDeck()
    shuffleDeck(deck)
    numplayers = 4 #input("Number of Players (2-6)")
    numplayers = int(numplayers)
    game(numplayers, deck)
 
if __name__ == "__main__":
    main()