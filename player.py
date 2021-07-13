

class Player:
    '''Representation of player'''
    def __init__(self):
        self.money = 5000
        self.bet = ''
        self.moves = ['(H)it', '(S)tand']
        self.cards = []
        
    def countPoints(self):
        self.points = 0
        for rank, suit in self.cards:
            if rank.isdecimal() and int(rank) in range(2, 11):# Number cards are worth their number value
                self.points += int(rank)
            if rank in ('King', 'Queen', 'Jack'):
                #Face cards are worth 10 points
                self.points += 10
            if rank == 'Ace':      
                self.points += 11
        # Ace are worth 11 or 1
        for rank, suit in self.cards:
            if rank == 'Ace' and self.points > 21:
                self.points -= 10
        
    def displayCards(self):
        for i, card in enumerate(self.cards):
            if i != 0:
              print(', ', end='')  
            print(' of '.join(i for i in card), end='')
        print()
        