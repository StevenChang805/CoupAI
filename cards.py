
class Card:
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.assign_actions(name)

    # start of method assign()
    def assign_actions(self, name):
        if name == 'Ambassador':
            self.actions.append('exchange')
            self.actions.append('block_steal')
            return
        if name == 'Assassin':
            self.actions.append('assassinate')
            return
        if name == 'Captain':
            self.actions.append('steal')
            self.actions.append('block_steal')
            return
        if name == 'Contessa':
            self.actions.append('block_assassinate')
            return
        if name == 'Duke':
            self.actions.append('tax')
            self.actions.append('block_foreign_aid')
            return
    # end of method assign()
