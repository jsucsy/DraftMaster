'''
Created on Jul 30, 2013

@author: JSU
'''
from Tkinter import *
import Config as cfg

TEAMS = {}
PLAYERS = {}
DRAFT_ORDER = []



def btn_pullteams_call():
    pullteams("%s%s" % (REFDIR, "teams_test.txt"))
    for team in DRAFT_ORDER:
        print TEAMS[team][0]

def btn_startdraft_call():
    draftlive = Toplevel()
    draftlive.title("Drafting")
    
    buttons = []
    btn_finishdraft = Button(draftlive, text = "Finish Draft", command = draftlive.destroy())
    buttons.append(btn_finishdraft)
    
    [x.pack() for x in buttons]
    



def pullteams(sourcefile):
    with open(sourcefile, 'rb+') as source:
        team_order = []
        for line in source:
            fields = line.split('|')
            team_order.append(fields[0])
            TEAMS[fields[0]] = fields[1:-1]
        if cfg.is_snake:
            print team_order
            for x in range(cfg.num_rounds):
                if x % 2 == 1:
                    for team in reversed(team_order):
                        DRAFT_ORDER.append(team)
                else:
                    for team in team_order:
                        DRAFT_ORDER.append(team)

def runframe():
    buttons = []
    btn_pullteams = Button(MASTER, text = "Pull Teams", command = btn_pullteams_call)
    buttons.append(btn_pullteams)    
    btn_startdraft = Button(MASTER, text = "Start Draft", command = btn_startdraft_call)
    buttons.append(btn_startdraft)
    
    [x.pack() for x in buttons]
    
    mainloop()

if __name__ == '__main__':
    MASTER = Tk()
    REFDIR = "C:\\dropbox\\football\\draftmaster\\"
    
    runframe()


