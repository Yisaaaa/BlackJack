'''Black Jack'''

import sys
import time
from deck import Deck 
from player import Player
from dealer import Dealer

class BlackJack:# Main class
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        
    def main(self):
        print('''Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''') # Intro
        print()
    
        while True:# Main loop
            # Check if player has money left
            if self.player.money == 0:
                print()
                print("Oh boy, your'e broke")
                print("Gambling isn't really cool")
                print('Thanks for playing!')
                sys.exit()
                
            # Set initial card for player and dealer.
            self.player.cards = self.deck.initialCards()
            self.dealer.cards = self.deck.initialCards()
            
            # Get player's bet
            self._getPlayerBet()
            
            # Display player and dealer's stats
            self._displayStats()
            
            # Check if anyone got blackjack
            if self.isBlackJack():
                self._displayStats(hideFirstCard=False)
                input('Press Enter to continue...')
                print('\n')
                continue
            
            # Handle Player move 
            while True:# Keep looping until player bust or stand or double down.
                move = self._getPlayerMove()
                
                # Handle Player move 
                self._handlePlayerMove(move)
                
                if self.player.points > 21 or move == 'S' or move == 'D': # End player's move if either player bust, stand, or double.
                    break

            #Determine who's the winner
            self._checkWinner()
            


    def _getPlayerBet(self):
        '''Ask player for bet'''
        print('Money: {}'.format(self.player.money))
        while True: # Keep looping until player enter a valid bet.
            bet = input('Enter your bet (1-{} or QUIT)> '.format(self.player.money))
            if bet.isdecimal() and 1<=int(bet)<=self.player.money:
                self.player.bet = int(bet)
                break
            if bet == 'QUIT':
                print('\nThank you for playing!')
                sys.exit()
            
    def _getPlayerMove(self):
        '''Ask player for move'''
        moves = self.player.moves[:]
        if len(self.player.cards) == 2 and self.player.bet < self.player.money:
            moves.append('(D)ouble')   
            movePrompt = ', '.join(move for move in moves)
        else:
            movePrompt = ', '.join(move for move in moves)
        
        while True: # Keep looping until player enter a valid move.
            move = input(movePrompt + ' > ')
            if move.upper() in ('H', 'S'):
                return move.upper()
            elif move.upper() == 'D' and '(D)ouble' in moves:
                return move.upper()
                
    def _handlePlayerMove(self, move):
        '''Handles moves made by player'''
        if move == 'H':
            newCard = self.deck.pullCard()
            self.player.cards.append(newCard)
            self.player.countPoints()
            self._displayStats()
            
        elif move == 'S':
            while self.dealer.points < 17:
                newCard = self.deck.pullCard()
                self.dealer.cards.append(newCard)
                self.dealer.countPoints()
                self._displayStats()
                print()
                time.sleep(.7)
            input('Press Enter to cotinue...')
            self._displayStats(False)
            
        elif move == 'D':
            newCard = self.deck.pullCard()
            self.player.cards.append(newCard)
            while True:
                additionalBet = int(input('Enter additional bet (1-{}): '.format(self.player.bet)))
                if 1 <= additionalBet <= self.player.bet:
                    self.player.bet += additionalBet
                    break
            while self.dealer.points < 17:
                newCard = self.deck.pullCard()
                self.dealer.cards.append(newCard)
                self.dealer.countPoints()
                self._displayStats()
            input('Press Enter to continue...')
            self._displayStats(False)
    
    def _displayStats(self, hideFirstCard=True):
        '''display both player and dealer's stats'''
        self.player.countPoints()
        self.dealer.countPoints()
        print()
        if hideFirstCard:
            print('Dealer: ?')
            self.dealer.displayCards(hideFirstCard)
            print()
            print('Player: {}'.format(self.player.points))
            self.player.displayCards()
        
        else:
            print('Dealer: {}'.format(self.dealer.points))
            self.dealer.displayCards(hideFirstCard)
            print()
            print('Player: {}'.format(self.player.points))
            self.player.displayCards()
            
    def _checkWinner(self):
        '''Determine who wins the game'''
        # Player wins if:
        if self.dealer.points < self.player.points <= 21:
            self.player.money += self.player.bet
            print('You win ${}!'.format(self.player.bet))
        elif self.dealer.points > 21:
            self.player.money += self.player.bet
            print('Dealer bust, you win ${}!'.format(self.player.bet))
        # Player loses if:
        elif self.player.points < self.dealer.points <= 21:
            self.player.money -= self.player.bet
            print('You lose!')
        elif self.player.points > 21:
            self.player.money -= self.player.bet
            print('Player bust, You lose!')
        # Tie if:
        elif self.player.points == self.dealer.points:
            print("It's a tie!")
        input('Press Enter to continue...')
        print('\n\n')
        
    def isBlackJack(self):
        print()
        if self.player.points == 21 and self.dealer.points == 21:
            print("Both sides got BlackJack, it's a tie")
            return True
        elif self.player.points == 21:
            print('You got BlackJack!')
            self.player.money += int(self.player.bet*1.5)
            return True
        elif self.dealer.points == 21:
            print('Dealer got BlackJack!')
            self.player.money -= self.player.bet
            return True
        

if __name__ == '__main__':
    BlackJack = BlackJack()
    BlackJack.main()
