'''
Created on Jul 30, 2013

@author: JSU
'''
from Tkinter import *
import Config as cfg



def pullteams(sourcefile):
    teams = {}
    draft_order = []
    with open(sourcefile, 'rb+') as source:
        team_order = []
        for line in source:
            fields = line.split('|')
            team_order.append(fields[0])
            teams[fields[0]] = fields[1:-1]
            teams[fields[0]][-1] = teams[fields[0]][-1].split('`')
        if cfg.is_snake:
            for x in range(cfg.num_rounds):
                if x % 2 == 1:
                    for team in reversed(team_order):
                        draft_order.append(team)
                else:
                    for team in team_order:
                        draft_order.append(team)
    
    return team_order, teams, draft_order

def runmain():
    root = Tk()
    root.title("Draft Master v0.1")
    
    mainframe = Frame(root, padx=5, pady=5)
    mainframe.grid(column=0,row=0,sticky=(N,S,E,W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0,weight=1)
    
    team_order, teams, draft_order = pullteams("%s%s" % (REFDIR,"teams_test.txt"))
    print teams
    
    colnum = 0
    for team in team_order:
        Label(mainframe, text=team).grid(column=colnum,row=0,sticky=(W,E))
        Listbox(mainframe).grid(column=colnum,row=1,sticky=(W,E))

        colnum+=1
        
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5,pady=5)

    root.mainloop()

if __name__ == '__main__':
    REFDIR = "C:\\dropbox\\football\\draftmaster\\"
    runmain()




#===============================================================================
# Failed attempt 1
#===============================================================================
# TEAMS = {}
# PLAYERS = {}
# DRAFT_ORDER = [] 
# def btn_pullteams_call():
#     pullteams("%s%s" % (REFDIR, "teams_test.txt"))
# 
# def btn_startdraft_call():
#     draftlive = Toplevel()
#     draftlive.title("Drafting")
#     
#     redraw_draftstatus(draftlive)
#     
#     draftbox = Frame(draftlive, height=480, width = 640, relief= SUNKEN)
#     draftbox.pack()
# 
#     buttons = []    
#     buttons.append(Button(draftlive, text = "Make pick", command = update_draft(draftbox)))
#     buttons.append(Button(draftlive, text = "Finish Draft", command = draftlive.destroy))
#     [x.pack() for x in buttons]
#     
#     
#     
# 
# 
# def pullteams(sourcefile):
#     with open(sourcefile, 'rb+') as source:
#         team_order = []
#         for line in source:
#             fields = line.split('|')
#             team_order.append(fields[0])
#             TEAMS[fields[0]] = fields[1:-1]
#         if cfg.is_snake:
#             print team_order
#             for x in range(cfg.num_rounds):
#                 if x % 2 == 1:
#                     for team in reversed(team_order):
#                         DRAFT_ORDER.append(team)
#                 else:
#                     for team in team_order:
#                         DRAFT_ORDER.append(team)
# 
# def runframe():
#     root = Tk()
#     root.title("Draft Master v0.1")
#     
#     
#     
#     buttons = []
#     buttons.append(Button(MASTER, text = "Pull Teams", command = btn_pullteams_call))
#     buttons.append(Button(MASTER, text = "Start Draft", command = btn_startdraft_call))
#     buttons.append(Button(MASTER, text = "Exit Program", command = MASTER.destroy))
#     
#     [x.pack() for x in buttons]
#     
#     mainloop()
# 
# if __name__ == '__main__':
#     MASTER = Tk()
#     
#     
#     runframe()


