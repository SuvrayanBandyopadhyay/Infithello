#We import the nescessary libraries 
import importlib
import time
import copy
import sys
from matplotlib import pyplot as plt
from gamestate import GameState
#To give timeouts to processes...
from threading import Thread
#To find all files
import os
import traceback


turn_limit = 8
#Get the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
#Bot directory
dir_bot = dir_path+"/bots"


#Get all bots
bots = list()
for file in os.listdir(dir_bot):
    if file.endswith(".py"):
        file = file[0:-3]
        bots.append(file)


#The tally of all the points
points = [0]*len(bots)

#Playing all bots against one another
for i in range(len(bots)):
    for j in range(len(bots)):
        if(i==j):
            continue
        #The starting gamestate
        game_state= GameState()

        #Define the players
        File1 = importlib.import_module("bots."+bots[i])
        File2 = importlib.import_module("bots."+bots[j])

        #Play match
        print("Match between "+bots[i]+"(Player 1) and "+bots[j]+"(Player2)")

        #The winner
        winner = -1

        #Get the player functions
        try:
            Player1 = getattr(File1,"play")
        except:
            print("INTERNAL ERROR FOR PLAYER 1")
            winner = 1

        try:
            Player2 = getattr(File2,"play")
        except:
            print("INTERNAL ERROR FOR PLAYER 2")
            winner = 0

        
        #Store the functions
        players = [Player1,Player2]

    
        #The timeout limit
        timeout = 1 #Each player gets 1s

        #While turns still exist
        winner = -1
        while game_state.turns < 2*turn_limit:

            #The player number
            pno = game_state.turns%2
            print("TURN ",(int)(game_state.turns/2))
            print("Player ")
            #Create a copy of the game state
            game_state_copy = copy.deepcopy(game_state)
            result = [-1,-1]
            try:
                if(pno==0):
                    p = Thread(target=Player1,args=(turn_limit,(int)(game_state_copy.turns/2),pno,game_state_copy.board,result))
                else:
                    p = Thread(target=Player2,args=(turn_limit,(int)(game_state_copy.turns/2),pno,game_state_copy.board,result))
                
                p.daemon = True
                p.start()
                p.join(timeout=timeout)

                #If it cant complete it in time
                if p.is_alive():
                    if(pno==0):
                        print("Player 1 has not completed it's move in time")
                        winner = 1
                        break
                    else:
                        print("Player 2 has not completed it's move in time")
                        winner = 0
                        break    
                #Resolve the action
                value = game_state.resolveAction(result[0],result[1],pno)
                if value == -1:
                    print("Player ",(pno+1)," has given an incorrect output ",result)
                    if(pno==0):
                        winner = 1
                        break
                    else:
                        winner = 0
                        break         
                
            except Exception as e:
                tb = traceback.extract_tb(e.__traceback__)
                filename, line, func, text = tb[-1]  # Get the last traceback entry
                print(f"Exception occurred in {filename} at line {line} in function {func}: {text}")
                print("EXCEPTION ",e)
                
                if(pno == 1):
                    print("Player 1's code could not be run")
                    winner = 1
                    break

                            
                if(pno == 2):
                    print("Player 2's code could not be run")
                    winner = 0
                    break
            #Display the board
            game_state.display()
            

        #Check the winner
        if(winner == -1):
            winner = game_state.winner()

        match(winner):
            case -1:
                print('Draw!')
                points[i]+=0.5
                points[j]+=0.5
            case 0:
                print(bots[i]+'(Player 1) wins!')
                points[i]+=1
            case 1:
                print(bots[j]+'(Player 2) wins!')
                points[j]+=1      

#Print the points
for i in range(0,len(bots)):
    print(bots[i],":",points[i])
input()

        
        
