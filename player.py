class Player:
    def __init__(self, turn_number):
        self.turn_number = turn_number
        self.cards = []

    def take_cards(self, deck):
        for i in deck[:]:
            self.cards.append(deck[i])
            deck.remove(i)

