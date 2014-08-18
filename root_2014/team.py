'''
Created on Aug 15, 2014

@author: jsu
'''

class Team:
    def __init__(self, name='', owner='', id='', budget = 200):
        self.name = name
        self.owner = owner
        self.players = []
        self.id = id
        self.budget = budget
        
    def name(self, name):
        self.name = name
        
    def owner(self, owner):
        self.owner = owner
        
    def show(self):
        print 'Name: %s' % self.name
        print 'Owner: %s' % self.owner
        print '# Players: %s' % len(self.players)
        print 'Budget: $%s' % self.budget
        
    def draft(self, player, cost):
        self.players.append(player)
        self.budget -= cost
        
    def roster(self):
        for player in self.players:
            print player