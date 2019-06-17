from coup import Coup

game = Coup(4)
game.distribute_cards()

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\t\t\t\tPlayer Info:")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for i in range(game.num_players):
    print("Player", str(i+1), "has the following cards:")
    for j in range(len(game.players[i].deck)):
        print(game.players[i].deck[j].name, "which can do the following actions:", game.players[i].deck[j].actions)
    print("In summary, he has the following actions", game.players[i].actions)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\t\t\t\tDeck Info")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(game.game_deck)

