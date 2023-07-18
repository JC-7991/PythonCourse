import random

suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
           'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:

    def __init__(self):

        self.deck = []
        for suit in suits:
            for rank in ranks:
                pass
    
    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        pass
    
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} card(s).'