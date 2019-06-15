from cards import Card


class Player:
    def __init__(self, turn_number):
        self.turn_number = turn_number
        self.cards = []
        self.deck = []
        self.coins = 2

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
