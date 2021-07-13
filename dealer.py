

class Dealer:
    def __init__(self):
        self.cards = []
        self.points = 0
        
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
        
    def displayCards(self, hide):
        for i, card in enumerate(self.cards):
            if not hide:
                if i != 0:
                    print(', ', end='')  
                print(' of '.join(i for i in card), end='')
            else: # Hide first card if hide is True
                if i == 0:
                    card = '???'
                    print(card, end='')
                else:
                    print(', ', end='')
                    print(' of '.join(i for i in card), end='')
        print()
        