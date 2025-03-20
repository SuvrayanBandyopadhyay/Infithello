#The gamestate class
class GameState:
    def __init__(self)->None:
        self.board = [['_','_','_','_'],['_','W','B','_'],['_','B','W','_'],['_','_','_','_']]
        self.turns =0

    #Resolves an action
    def resolveAction(self,x,y,color)->int:
        self.turns += 1
        #Out of bound errors
        if(x>=len(self.board[0])):
            return -1
        if(x<0):
            return -1

        if(y>=len(self.board)):
            return -1
        if(y<0):
            return -1
        
        #Check if blank place
        if(self.board[y][x]!='_'):
            return -1
        
        #Check if there is an adjacent piece
        adjacent = False
        if(y-1>=0):
            if(self.board[y-1][x] in ('W','B')):
                adjacent = True
        
        
        if(y+1<len(self.board)):
            if(self.board[y+1][x] in ('W','B')):
                adjacent = True
        
        if(x-1>=0):
            if(self.board[y][x-1] in ('W','B')):
                adjacent = True

        if(x+1<len(self.board[0])):
            if(self.board[y][x+1] in ('W','B')):
                adjacent = True

        if(y+1<len(self.board) and x+1<len(self.board[0])):
            if(self.board[y+1][x+1] in ('W','B')):
                adjacent = True

        if(y+1<len(self.board) and x-1>=0):
            if(self.board[y+1][x-1] in ('W','B')):
                adjacent = True
        if(y-1>=0 and  x+1<len(self.board[0])):
            if(self.board[y-1][x+1] in ('W','B')):
                adjacent=True
        if(y-1>=0 and x-1>=0):
            if(self.board[y-1][x-1] in ('W','B')):
                adjacent=True

        if(adjacent==False):
            return -1
        
        #Add the piece to the gamestate
        #If black
        if(color==0):
            piece = 'B'
      
        else:
            piece = 'W'
  
        self.board[y][x] = piece

        #Flip the disks
        #For right
        for i in range(x+1,len(self.board[0])):
            if(self.board[y][i]=='_'):
                break
            if(self.board[y][i]==piece):
                for k in range(i,x,-1):
                    self.board[y][k] = piece
                break
        #For left
        for i in range(x-1,-1,-1):
            if(self.board[y][i]=='_'):
                break
            if(self.board[y][i]==piece):
                for k in range(i,x):
                    self.board[y][k] = piece
                break
        #For down
        for i in range(y+1,len(self.board)):

            if(self.board[i][x]=='_'):
                break
            if(self.board[i][x]==piece):
                
                for k in range(i,y,-1):
                    self.board[k][x] = piece
                break

        #For up
        for i in range(y-1,-1,-1):
            if(self.board[i][x]=='_'):
                break
            if(self.board[i][x]==piece):
                for k in range(i,y):
                    self.board[k][x] = piece
                break
        #Diagonals
        to_flip = []
        #For diagonal 1
        _x = x+1
        _y = y+1
        
        checked = []
        while(_x<len(self.board[0]) and _y<len(self.board)):
            checked.append((_x,_y))
            if(self.board[_y][_x]=='_'):
                
                break
            if(self.board[_y][_x]==piece):
                to_flip.extend(checked)
                break
            _x +=1
            _y +=1
        #Diagonal 2
        _x = x+1
        _y = y-1
        
       
        checked = []
        while(_x<len(self.board[0]) and _y>=0):
            checked.append((_x,_y))
            
            if(self.board[_y][_x]=='_'):
                break
            if(self.board[_y][_x]==piece):
                to_flip.extend(checked)
                break
            _x+=1
            _y-=1
        #Diagonal 3
        _x = x-1
        _y = y+1
        
        checked = []
        while(_x>=0 and _y<len(self.board)):
            checked.append((_x,_y))
            
            if(self.board[_y][_x]=='_'):
                break
            if(self.board[_y][_x]==piece):
                to_flip.extend(checked)
                break
            _x-=1
            _y+=1
        
        #Diagonal 4
        _x = x-1
        _y = y-1
        
        checked = []
        while(_x>=0 and _y>=0):
            checked.append((_x,_y))
            
            if(self.board[_y][_x]=='_'):
                break
            if(self.board[_y][_x]==piece):
                to_flip.extend(checked)
                break
            _x-=1
            _y-=1
        #Flip due to diagonals
        for flip in to_flip:
            self.board[flip[1]][flip[0]]=piece
        
        #Expand the board if required
        if(x==0):
            for row in self.board:
                row.insert(0,'_')
        elif(x==len(self.board[0])-1):
            for row in self.board:
                row.append('_')

        if(y==0):
            blank = ['_',]*len(self.board[0])
            self.board.insert(0,blank)
        elif(y==len(self.board)-1):
            blank = ['_',]*len(self.board[0])
            self.board.append(blank)

        #Return no error
        return 0

    #Display the board
    def display(self):
        for r in self.board:
            print(r)

    #Calculates the winner
    def winner(self)->int:
        black = 0
        white = 0
        for row in self.board:
            for r in row:
                if(r=='B'):
                    black+=1
                elif(r=='W'):
                    white+=1
        #If black wins
        if(black>white):
            return 0
        #If white wins
        elif(white>black):
            return 1
        #If tie
        else:
            return -1