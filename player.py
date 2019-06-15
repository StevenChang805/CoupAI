class Player:
    def __init__(self, turn_number):
        self.turn_number = turn_number
        self.cards = []
        self.coins = 2

    def take_cards(self, deck, num_cards):
        deck_copy = deck
        for i in range(num_cards):
            self.cards.append(deck[i])
            deck_copy = deck[i+1:len(deck)]

        return deck_copy


