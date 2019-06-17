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
        self.player_ids = []

        # initializes players
        for i in range(num_players):
            self.players.append(Player(i))
            self.player_ids.append(i)

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

    # start of function interpret_action()
    def interpret_action(self, player_id, action_name):
        if action_name == 'income':
            self.players[player_id].coins += 1
        if action_name == 'foreign_aid':
            self.players[player_id].coins += 2
        if action_name == 'coup':
            if self.players[player_id].coins < 7:
                print('Action failed. Player', player_id, 'does not have sufficient coins.')
            else:
                self.players[player_id].coins -= 7
                couped_player_id = self.players[player_id].select_player(self.player_ids)
                self.players[couped_player_id].lose_card()
        if action_name == 'exchange':
            self.players[player_id].cards.append(self.game_deck[0], self.game_deck[1])
            self.players[player_id].initialize_deck()
            returned_cards = self.players[player_id].return_cards(2)
            self.game_deck.append(returned_cards[0])
            self.game_deck.append(returned_cards[1])
        if action_name == 'assassinate':
            if self.players[player_id].coins < 3:
                print('Action failed. Player', player_id, 'does not have sufficient coins.')
            else:
                self.players[player_id].coins -= 3
                assassinated_player_id = self.players[player_id].select_player(self.player_ids)
                self.players[assassinated_player_id].lose_card()
        if action_name == 'steal':
            self.players[player_id].coins += 2
            # TODO: figure out how to make them steal from SOMEONE
            # see 'assassinate' for more details (have to make a general function that can be applied to coup & steal)
        if action_name == 'tax':
            self.players[player_id].coins += 3
        if action_name == 'block_steal':
            work_in_progress = True
            # TODO: have to make two different 'types' of actions: inflicted upon someone and not inflicted upon someone
            # create a function retaliate() which can return 'block_steal' if in player's list of actions
            # if the function doesn't return anything the action goes through
        if action_name == 'block_assassinate':
            work_in_progress = True
            # see action_name == 'block_steal' for more details
        if action_name == 'block_foreign_aid':
            work_in_progress = True
            # see action_name == 'block_foreign_aid' for more details

    # TODO: Function to remove a player's card when couped
    # TODO: Function to force player to coup when has more than 10 coins
    # TODO: Function to start a game and end when total number of player reaches one


