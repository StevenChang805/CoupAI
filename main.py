from coup import Coup

game = Coup(4)
game.distribute_cards()
print(game.players[0].cards)
print(game.deck)
