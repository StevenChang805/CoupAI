from cards import Card
import random
from collections import Counter

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
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
        self.remove_duplicate_actions()
    # end of method initialize_deck()

    # start of method make_action()
    def make_action(self):
        card_index = random.randint(0, len(self.actions)-1)
        return self.actions[card_index]
    # end of method make_action()

    # start of method return_cards()
    def return_cards(self, num_cards):
        returned_cards = []
        for i in range(num_cards):
            returned_cards.append(self.deck[random.randint(len(self.deck))])
            self.deck.remove(self.deck.index(returned_cards[i]))
        return returned_cards
    # end of method return_cards

    # start of method remove_duplicate_actions()
    def remove_duplicate_actions(self):
        actions_copy = self.actions
        for i in range(len(self.actions)-1):
            action_dict = dict(Counter(self.actions))
            if action_dict.get(self.actions[i]) > 1:
                actions_copy.remove(self.actions[i])
        self.actions = actions_copy
    # end of method remove_duplicate_actions()

    # start of method select_player()
    def select_player(self, player_ids):
        selected_player_id_index = self.player_id
        # making it foolproof
        while selected_player_id_index == self.player_id:
            selected_player_id_index = random.randint(0, len(player_ids))
        return player_ids[selected_player_id_index]
    # end of method select_player()