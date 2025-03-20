import random
def play(total_turns,turn_no,color,state,result):
    candidate = []

 
    for y in range(0,len(state)):
        for x in range(0,len(state[0])):
            if(state[y][x]!='_'):
                continue

            #Check if there is an adjacent piece
            adjacent = False
            if(y-1>=0):
                if(state[y-1][x] in ('W','B')):
                    adjacent = True
            
            
            if(y+1<len(state)):
                if(state[y+1][x] in ('W','B')):
                    adjacent = True
            
            if(x-1>=0):
                if(state[y][x-1] in ('W','B')):
                    adjacent = True

            if(x+1<len(state[0])):
                if(state[y][x+1] in ('W','B')):
                    adjacent = True

            if(y+1<len(state) and x+1<len(state[0])):
                if(state[y+1][x+1] in ('W','B')):
                    adjacent = True

            if(y+1<len(state) and x-1>=0):
                if(state[y+1][x-1] in ('W','B')):
                    adjacent = True
            if(y-1>=0 and  x+1<len(state[0])):
                if(state[y-1][x+1] in ('W','B')):
                    adjacent=True
            if(y-1>=0 and x-1>=0):
                if(state[y-1][x-1] in ('W','B')):
                    adjacent=True

            if adjacent == True:
                candidate.append((x,y))
    
    #SHOULD NOT HAPPEN THOUGH
    if(len(candidate)==0):
        result[0] =0
        result[1] =0
        return
    val = random.randint(0,len(candidate)-1)
    t = candidate[val]

    result[0]=t[0]
    result[1]=t[1]


    
