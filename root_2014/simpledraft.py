'''
Created on Aug 14, 2014

@author: jsu
'''
import config as c
import cPickle as pickle
import os, platform
from team import Team

        
# ---------------private-ish functions-----------
def set_players_yahoo():
    sourcefile_qb = c.workingdir + '20140815_yahoo_qb.csv'
    sourcefile_rb = c.workingdir + '20140815_yahoo_rb.csv'
    sourcefile_wr = c.workingdir + '20140815_yahoo_wr.csv'
    sourcefile_te = c.workingdir + '20140815_yahoo_te.csv'
    sourcefile_ki = c.workingdir + '20140815_yahoo_ki.csv'
    
    
    c.qb, c.qb_headers = parse_yahoo(sourcefile_qb)
    #c.rb, c.rb_headers = parse_yahoo(sourcefile_rb)
    #c.wr, c.wr_headers = parse_yahoo(sourcefile_wr)
    #c.te, c.te_headers = parse_yahoo(sourcefile_te)
    #c.ki, c.ki_headers = parse_yahoo(sourcefile_ki)
    
    #return qb, rb, wr, qb_headers,rb_headers, wr_headers

def parse_yahoo(sourcefile):
    players = []
    headers = []
    with open(sourcefile, 'rb+') as source:
        linenum = 0
        for line in source:
            fields = line.split('|')
            if linenum == 0:
                headers = fields
            else:
                fields[0] = fields[0].upper()
                player = fields
                players.append(player)
            linenum += 1
    
    return players, headers

def setbackup():
    temp = raw_input('Set backup name, n for no backup: ')
    if temp.lower() != 'n':
        c.backup = 'backup\\%s' % temp
        os.mkdir(c.workingdir + c.backup)
        c.backup = 'backup\\%s\\' % temp


# ----------- functions for live draft-----------------
def setupdraft():
    #qb, rb, wr, qb_headers,rb_headers, wr_headers = set_players_yahoo()
    set_players_yahoo()
    setteams()
    setbackup()
    backup()
    avail()

def setteams():
    leagues = []
    for filename in os.listdir(c.workingdir + 'setup'):
        if 'teams' in filename:
            leagues.append(filename)
    
    for league in leagues:
        print "%s: %s" % (leagues.index(league), league)        
    leaguenum = int(raw_input('Select league number: '))
    
    with open(c.workingdir + 'setup\\%s' % leagues[leaguenum], 'rb+') as source:
        counter = 0
        for line in source:
            fields = line.split('|')
            teamtemp = Team(fields[0], fields[1], counter)
            c.teams.append(teamtemp)

def nomq(name=''):
    nomtemp=[]
    nomtemp.append('qb')
    for player in c.qb:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom   
    return

def nomr(name=''):
    nomtemp=[]
    nomtemp.append('rb')
    for player in c.rb:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom   
    return

def nomw(name=''):
    nomtemp=[]
    nomtemp.append('wr')
    for player in c.wr:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom
    return

def nomt(name=''):
    nomtemp=[]
    nomtemp.append('te')
    for player in c.te:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom
    return

def nomk(name=''):
    nomtemp=[]
    nomtemp.append('ki')
    for player in c.ki:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom
    return

def nomd(name=''):
    nomtemp=[]
    nomtemp.append('ds')
    for player in c.ds:
        if name.upper() in player[0]:
            nomtemp.append(player)
    
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp     
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player)
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
            
    print c.nom
    return

def qb(display = 5):
    #print "Display: %s" % display
    print c.qb_headers
    counter = 0
    while counter < display:        
        print c.qb[counter]
        counter += 1
def rb(display = 5):
    #print "Display: %s" % display
    print c.rb_headers
    counter = 0
    while counter < display:        
        print c.rb[counter]
        counter += 1        
def wr(display = 5):
    #print "Display: %s" % display
    print c.wr_headers
    counter = 0
    while counter < display:        
        print c.wr[counter]
        counter += 1        
def te(display = 5):
    #print "Display: %s" % display
    print c.te_headers
    counter = 0
    while counter < display:        
        print c.te[counter]
        counter += 1        
def ki(display = 5):
    #print "Display: %s" % display
    print c.ki_headers
    counter = 0
    while counter < display:        
        print c.ki[counter]
        counter += 1        
def ds(display = 5):
    #print "Display: %s" % display
    print c.ds_headers
    counter = 0
    while counter < display:        
        print c.ds[counter]
        counter += 1
        
def teams():
    for team in c.teams:
        team.show()
        
def avail():
    print "Available QB: %s" % len(c.qb)
    print "Available RB: %s" % len(c.rb)
    print "Available WR: %s" % len(c.wr)
    print "Available TE: %s" % len(c.te)
    print "Available KI: %s" % len(c.ki)
    #print "Available DS: %s" % len(ds) 
    
def showme():
    funcs = ['avail','setfordraft','qb','rb','wr','te','ki','ds',
             'nomq','nomr','nomw','nomt','nomk','nomd',
             'backup','recover', 'teams', 'setnode',
             'draft', 'roster']
    for func in funcs:
        print func
    

def backup():
    
    pickle.dump(c.qb, open(c.workingdir + c.backup + 'qb.pkl', 'wb+'))
    pickle.dump(c.rb, open(c.workingdir + c.backup + 'rb.pkl', 'wb+'))
    pickle.dump(c.wr, open(c.workingdir + c.backup + 'wr.pkl', 'wb+'))
    pickle.dump(c.te, open(c.workingdir + c.backup + 'te.pkl', 'wb+'))
    pickle.dump(c.ki, open(c.workingdir + c.backup + 'ki.pkl', 'wb+'))
    pickle.dump(c.ds, open(c.workingdir + c.backup + 'ds.pkl', 'wb+'))
    
    pickle.dump(c.qb_headers, open(c.workingdir + c.backup + 'qb_headers.pkl', 'wb+'))
    pickle.dump(c.rb_headers, open(c.workingdir + c.backup + 'rb_headers.pkl', 'wb+'))
    pickle.dump(c.wr_headers, open(c.workingdir + c.backup + 'wr_headers.pkl', 'wb+'))
    pickle.dump(c.te_headers, open(c.workingdir + c.backup + 'te_headers.pkl', 'wb+'))
    pickle.dump(c.ki_headers, open(c.workingdir + c.backup + 'ki_headers.pkl', 'wb+'))
    pickle.dump(c.ds_headers, open(c.workingdir + c.backup + 'ds_headers.pkl', 'wb+'))
    
    pickle.dump(c.nom, open(c.workingdir + c.backup + 'nom.pkl', 'wb+'))
    
    pickle.dump(c.teams, open(c.workingdir + c.backup + 'teams.pkl', 'wb+'))

    return

def recover():
    saves = os.listdir(c.workingdir + '\\backup\\')
    counter = 0
    for save in saves:
        print "%s: %s" % (counter, save)
        
    torecover = int(raw_input("Pick draft to recover: "))
    c.backup = 'backup\\%s\\' % saves[torecover]
    print c.backup    
    
    c.qb = pickle.load(open(c.workingdir + c.backup + 'qb.pkl', 'rb+'))
    c.rb = pickle.load(open(c.workingdir + c.backup + 'rb.pkl', 'rb+'))
    c.wr = pickle.load(open(c.workingdir + c.backup + 'wr.pkl', 'rb+'))
    c.te = pickle.load(open(c.workingdir + c.backup + 'te.pkl', 'rb+'))
    c.ki = pickle.load(open(c.workingdir + c.backup + 'ki.pkl', 'rb+'))
    c.ds = pickle.load(open(c.workingdir + c.backup + 'ds.pkl', 'rb+'))
    
    c.qb_headers = pickle.load(open(c.workingdir + c.backup + 'qb_headers.pkl', 'rb+'))
    c.rb_headers = pickle.load(open(c.workingdir + c.backup + 'rb_headers.pkl', 'rb+'))
    c.wr_headers = pickle.load(open(c.workingdir + c.backup + 'wr_headers.pkl', 'rb+'))
    c.te_headers = pickle.load(open(c.workingdir + c.backup + 'te_headers.pkl', 'rb+'))
    c.ki_headers = pickle.load(open(c.workingdir + c.backup + 'ki_headers.pkl', 'rb+'))
    c.ds_headers = pickle.load(open(c.workingdir + c.backup + 'ds_headers.pkl', 'rb+'))
    
    c.nom = pickle.load(open(c.workingdir + c.backup + 'nom.pkl', 'rb+'))
    
    c.teams = pickle.load(open(c.workingdir + c.backup + 'teams.pkl', 'rb+'))
    
    return

def saveas():
    setbackup()
    backup()

def setnode():
    if platform.node() == 'JoshLaptop':
        c.workingdir = 'c:\\users\\josh\\dropbox\\football\\temp\\'

def draft(team, cost = 0):
    player = c.nom
    player.append(team)
    player.append(cost)
    c.drafted.append(player)
    c.teams[team].draft(player, cost)
    
    
def roster(team):
    c.teams[team].roster()

def testall():
    
    setupdraft()
    #setteams()
    backup()
    #recover()
    qb()
    teams()    
# --------------classes-------------------


if __name__ == '__main__':
    testall()
    