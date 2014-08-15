'''
Created on Aug 15, 2014

@author: jsu
'''

class Team:
    def __init__(self, name='', owner='', id=''):
        self.name = name
        self.owner = owner
        self.players = []
        self.id = id
        
    def name(self, name):
        self.name = name
        
    def owner(self, owner):
        self.owner = owner
        
    def show(self):
        print 'Name: %s' % self.name
        print 'Owner: %s' % self.owner
        print '# Players: %s' % len(self.players)
        