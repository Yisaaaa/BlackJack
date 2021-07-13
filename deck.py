
from random import shuffle

# Set the constants
HEART   = chr(9829)
DIAMOND = chr(9830)
CLUB    = chr(9827)
SPADE   = chr(9824)


class Deck:
    '''Representation of a 52 card deck'''
    def __init__(self):
        self._prepareCard()
        
    
    def _prepareCard(self):
        self.cards = []
        for suit in (HEART, DIAMOND, SPADE, 
        CLUB):
            for rank in range(2, 11):# Number cards
                self.cards.append((str(rank), suit))
            for rank in ('Ace', 'King', 'Queen',
            'Jack'): # Face cards
                self.cards.append((str(rank), suit))
        shuffle(self.cards)
        return self.cards
        
    def initialCards(self):
        cards = []
        for _ in range(2):
            cards.append(self.cards.pop())
        return cards
    
    def pullCard(self):
        card = self.cards.pop()
        return card