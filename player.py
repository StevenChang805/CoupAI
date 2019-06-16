from cards import Card
import random

class Player:
    def __init__(self):
        self.cards = []
        self.deck = []
        self.coins = 2
        self.actions = []

    # start of method take_cards()
    def take_cards(self, deck, num_cards):
        deck_copy = deck
        for i in range(num_cards):
            self.cards.append(deck[i])
            deck_copy = deck[i + 1:len(deck)]

        return deck_copy

    # end of method take_cards()

    # start of method initialize_deck()
    def initialize_deck(self):
        for i in range(len(self.cards)):
            self.deck.append(Card(self.cards[i]))
        for i in range(len(self.deck)):
            self.actions.append(self.deck[i].actions)

    def make_action(self):
        action_index = random.randint(0, len(self.actions))
        return self.actions[action_index]
