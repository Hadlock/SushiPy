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
    for i, card in enumerate(deck): # pylint: disable=unused-variable
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
    self.strategy = random.randint(0,6) # each player picks a random strategy
    self.hand = []
    self.passs = []
    self.played = []

def dealcards(players, numplayers, deck):
    for p in range(numplayers):
        print("for p in numplayers")
        n = SushiPlayer(0,0,0,[],[],[])
        players.append(n)
        for r in range(8): # pylint: disable=unused-variable
            card = deck.pop()
            players[p].hand.append(card)
        attrs = vars(players[p])
        print(', '.join("%s: %s" % item for item in attrs.items()))

def passcards(players):
    for p in range(len(players)):
        for c in range(len(players[p].passs)): # pylint: disable=unused-variable
            card = players[p].passs.pop()
            print(p)
            players[p].hand.append(card)
            attrs = vars(players[p])
            print(', '.join("%s: %s" % item for item in attrs.items()))

def remove(players, card, i):
    # remove card from hand
    players[i].hand.remove(card)

def strategy0(players, deck, i):
    # the most simple strategy, play one card at random
    print("playing strategy 0")
    # play a card
    card = players[i].hand.pop()
    players[i].played.append(card)
    return card

def strategy1(players, deck, i):
    # try and collect nigiri
    print("playing strategy 1")
    card = "strategy 1 placeholder"
    played = 0
    if 'W' in players[i].hand:
        # play wasabi
        if len(players[i].played) > 1:
            if players[i].played[-1] != 'W':
                print("WASABI FOUND! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                card = players[i].hand[players[i].hand.index('W')]
                players[i].played.append(card)
                remove(players, card, i)
        elif len(players[i].played) == 0:
            print("WASABI FOUND! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            card = players[i].hand[players[i].hand.index('W')]
            players[i].played.append(card)
            remove(players, card, i)

        else:
            strategy0(players, deck, i)
        played += 1
    
    if 'n' in players[i].hand:
        if played == 0:
            # take a squid nigiri if possible, most points
            card = players[i].hand[players[i].hand.index('n')]
            players[i].played.append(card)
            remove(players, card, i)
            played += 1

    if 'N' in players[i].hand:
        if played == 0:
            # if no squid in hand, pick salmon, 2nd most points
            card = players[i].hand[players[i].hand.index('N')]
            players[i].played.append(card)
            remove(players, card, i)
            played += 1

    if len(players[i].played) > 0:
        if players[i].played[-1] == 'W':
            if played == 0:
                # only grab egg nigiri if wasabi ready
                if 'E' in players[i].hand:
                    # else get egg
                    card = players[i].hand[players[i].hand.index('E')]
                    players[i].played.append(card)
                    remove(players, card, i)
                    played += 1


    if played == 0:
        print("no good nigiri, pick something random;")
        # if no nigiri or valid wasabi, grab something random
        strategy0(players, deck, i)
        played += 1


    return card

def strategy2(players, deck, i):
    # all tempura, all the time
    card = "strategy 2 card placeholder"
    if 'T' in players[i].hand:
        card = players[i].hand[players[i].hand.index('T')]
        players[i].played.append(card)
        remove(players, card, i)

    else:
        # if no tempura, grab something random
        strategy0(players, deck, i)

    return card

def strategy3(players, deck, i):
    # maki strategi m M w
    card = "strategy 3 card placeholder"
    played = 0
    if 'm' in players[i].hand:
        if played == 0:
            card = players[i].hand[players[i].hand.index('m')]
            players[i].played.append(card)
            remove(players, card, i)
            played += 1
    if 'M' in players[i].hand:
        if played == 0:
            card = players[i].hand[players[i].hand.index('M')]
            players[i].played.append(card)
            remove(players, card, i)
            played += 1
    if 'w' in players[i].hand:
        if played == 0:
            card = players[i].hand[players[i].hand.index('w')]
            players[i].played.append(card)
            remove(players, card, i)
            played += 1
    if played == 0:
        # if no maki, grab something random
        strategy0(players, deck, i)

    return card

def strategy4(players, deck, i):
    # all sashimi, all the time
    card = "strategy 4 card placeholder"
    if 'S' in players[i].hand:
        card = players[i].hand[players[i].hand.index('S')]
        players[i].played.append(card)
        remove(players, card, i)

    else:
        # if no sashimi, grab something random
        strategy0(players, deck, i)

    return card

def strategy5(players, deck, i):
    # all dumplings, all the time
    card = "strategy 5 card placeholder"
    if 'D' in players[i].hand:
        card = players[i].hand[players[i].hand.index('D')]
        players[i].played.append(card)
        remove(players, card, i)

    else:
        # if no dumplings, grab something random
        strategy0(players, deck, i)

    return card

def strategy6(players, deck, i):
    # favor the puddin'
    card = "strategy 6 card placeholder"
    if 'P' in players[i].hand:
        card = players[i].hand[players[i].hand.index('P')]
        players[i].played.append(card)
        remove(players, card, i)

    else:
        # if no puddin', grab something random
        strategy0(players, deck, i)

    return card


def playstrategy(players, deck, i):
    # a strategy is just a method to pick which card to play next

    card = "placeholder" # pylint: disable=unused-variable
    
    if players[i].strategy is 0:
        card = strategy0(players, deck, i)
    if players[i].strategy is 1:
        card = strategy1(players, deck, i)
    if players[i].strategy is 2:
        card = strategy2(players, deck, i)
    if players[i].strategy is 3:
        card = strategy3(players, deck, i)
    if players[i].strategy is 4:
        card = strategy4(players, deck, i)
    if players[i].strategy is 5:
        card = strategy5(players, deck, i)
    if players[i].strategy is 6:
        card = strategy6(players, deck, i)


    return card

def playround(players, deck):
    phases = len(players[0].hand)
    for p in range(phases):
    # for each phase
        for i in range(len(players)):
        # for each player

            # if there are passed cards, put them in your hand
            if len(players[i].passs) > 0:
                for pas in players[i].passs: # pylint: disable=unused-variable
                    card = players[i].passs.pop()
                    players[i].hand.append(card)


            card = playstrategy(players, deck, i)
            
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
    
    # TODO: debug maki score calc, sometimes returns 0
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