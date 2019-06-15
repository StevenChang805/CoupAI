from coup import Coup

game = Coup(4)
game.distribute_cards()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\t\t\t\tPlayer Info:")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for i in range(game.num_players):
    print("Player", str(i+1), "has the following cards:", game.players[i].cards)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\t\t\t\tDeck Info")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(game.deck)
