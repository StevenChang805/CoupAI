from player import Player

class Coup:
    def __init__(self, num_players):
        self.num_players = num_players
        self.game_deck = ['Ambassador', 'Ambassador', 'Ambassador',
                          'Assassin', 'Assassin', 'Assassin',
                          'Captain', 'Captain', 'Captain',
                          'Contessa', 'Contessa', 'Contessa',
                          'Duke', 'Duke', 'Duke']
        self.all_actions = ['income', 'foreign_aid', 'coup', 'exchange', 'assassinate', 'steal', 'tax',
                            'block_steal', 'block_assassinate', 'block_foreign_aid']
        self.players = []

        # initializes players
        for i in range(num_players):
            self.players.append(Player())

    # start of method shuffle_deck()
    def shuffle_deck(self):
        from random import shuffle
        shuffle(self.game_deck)

    # end of method shuffle_deck()

    # start of method distribute_cards()
    def distribute_cards(self):
        self.shuffle_deck()
        for i in range(len(self.players)):
            self.game_deck = self.players[i].take_cards(self.game_deck, 2)
            self.players[i].initialize_deck()
    # end of method distribute_cards()

    ##
    # TODO: Function to decode the action a player makes
    # TODO: Function to remove a player's card when couped
    # TODO: Function to force player to coup when has more than 10 coins
    # TODO: Function to start a game and end when total number of player reaches one


