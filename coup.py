
from player import Player
import random

class Coup:
    def __init__(self, num_players):
        self.num_players = num_players
        self.num_cards = 15
        # Ambassador ID is 0, and the three Ambassador cards are further divided into 0a, 0b, and 0c, and so forth for the other cards.
        self.deck = ['Ambassador', 'Ambassador', 'Ambassador', 'Assassin', 'Assassin', 'Assassin', 'Captain', 'Captain', 'Captain', 'Contessa', 'Contessa', 'Contessa', 'Duke', 'Duke', 'Duke']

        self.players = []

        # initializes players
        for i in range (num_players):
            self.players.append(Player(i))

    # start of method shuffle_deck()
    def shuffle_deck(self):
        n = len(self.deck)

        for i in range(n):
            for j in range (n - i - 1):
                chance = random.randint(0, 5)
                if chance >= 1:
                    self.deck[j], self.deck[j + 1] = self.deck[j + 1], self.deck[j]

        for i in range(n):
            for j in range (n - i - 1):
                chance = random.randint(0, 5)
                if chance >= 1:
                    self.deck[j], self.deck[j + 1] = self.deck[j + 1], self.deck[j]
    # end of method shuffle_deck()

    # start of method distribute_cards()
    def distribute_cards(self):
        self.shuffle_deck()
        for i in range(len(self.players)):
            self.deck = self.players[i].take_cards(self.deck, 2)
    # end of method distribute_cards()

