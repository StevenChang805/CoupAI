from cards import Card
import random

class Player:
    def __init__(self, player_id):
        self.cards = []
        self.deck = []
        self.coins = 2
        self.actions = ['income', 'foreign_aid']

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
        self.deck = []
        for i in range(len(self.cards)):
            self.deck.append(Card(self.cards[i]))
        for i in range(len(self.deck)):
            for j in range(len(self.deck[i].actions)):
                self.actions.append(self.deck[i].actions[j])

    def make_action(self):
        card_index = random.randint(0, len(self.actions)-1)
        return self.actions[card_index]

    def return_cards(self, num_cards):
        returned_cards = []
        for i in range(num_cards):
            returned_cards.append(self.deck[random.randint(len(self.deck))])
            self.deck.remove(self.deck.index(returned_cards[i]))
        return returned_cards
