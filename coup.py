
from player import Player
import random

class Coup:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = ['Ambassador', 'Ambassador', 'Ambassador',
                     'Assassin', 'Assassin', 'Assassin',
                     'Captain', 'Captain', 'Captain',
                     'Contessa', 'Contessa', 'Contessa',
                     'Duke', 'Duke', 'Duke']
        self.actions = ['income', 'foreign aid', 'coup', 'exchange', 'assassinate', 'steal', 'tax', '']

        self.players = []

        # initializes players
        for i in range(num_players):
            self.players.append(Player(i))

    # start of method shuffle_deck()
    def shuffle_deck(self):
        from random import shuffle
        shuffle(self.deck)
    # end of method shuffle_deck()

    # start of method distribute_cards()
    def distribute_cards(self):
        self.shuffle_deck()
        for i in range(len(self.players)):
            self.deck = self.players[i].take_cards(self.deck, 2)
    # end of method distribute_cards()

