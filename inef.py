#Rook Moves:
"""if self.whiteToMove:  
            i=1
            j=1
            k=1
            l=1
            while r-i >= 0 : # Vertical Top
                if self.board[r-i][c][0] =='-':
                    moves.append(Move((r, c), (r-i, c), self.board))
                    i+=1
                elif self.board[r-i][c][0] =='b':
                    moves.append(Move((r, c), (r-i, c), self.board))
                    break
                else:
                    break
            while r+j <= 7 : # Vertical Bot
                if self.board[r+j][c][0 ] =='-':
                    moves.append(Move((r, c), (r+j, c), self.board))
                    j+=1
                elif self.board[r+j][c][0] =='b':
                    moves.append(Move((r, c), (r+j, c), self.board))
                    break
                else:
                    break

            while c-k >= 0 : # Horisontal Left
                if self.board[r][c-k][0] =='-':
                    moves.append(Move((r, c), (r, c-k), self.board))
                    k+=1
                elif self.board[r][c-k][0] =='b':
                    moves.append(Move((r, c), (r, c-k), self.board))
                    break
                else:
                    break
            while c+l <= 7 : # Horisontal Right
                if self.board[r][c+l][0] =='-':
                    moves.append(Move((r, c), (r, c+l), self.board))
                    l+=1
                elif self.board[r][c+l][0] =='b':
                    moves.append(Move((r, c), (r, c+l), self.board))
                    break
                else:
                    break
        else:
            i=1
            j=1
            k=1
            l=1
            while r-i >= 0 : # Vertical Top
                if self.board[r-i][c][0] =='-':
                    moves.append(Move((r, c), (r-i, c), self.board))
                    i+=1
                elif self.board[r-i][c][0] =='w':
                    moves.append(Move((r, c), (r-i, c), self.board))
                    break
                else:
                    break
            while r+j <= 7 : # Vertical Bot
                if self.board[r+j][c][0 ] =='-':
                    moves.append(Move((r, c), (r+j, c), self.board))
                    j+=1
                elif self.board[r+j][c][0] =='w':
                    moves.append(Move((r, c), (r+j, c), self.board))
                    break
                else:
                    break

            while c-k >= 0 : # Horisontal Left
                if self.board[r][c-k][0] =='-':
                    moves.append(Move((r, c), (r, c-k), self.board))
                    k+=1
                elif self.board[r][c-k][0] =='w':
                    moves.append(Move((r, c), (r, c-k), self.board))
                    break
                else:
                    break
            while c+l <= 7 : # Horisontal Right
                if self.board[r][c+l][0] =='-':
                    moves.append(Move((r, c), (r, c+l), self.board))
                    l+=1
                elif self.board[r][c+l][0] =='w':
                    moves.append(Move((r, c), (r, c+l), self.board))
                    break
                else:
                    break """





#Bishop  Moves:
"""  if self.whiteToMove:      
            i=1
            j=1
            k=1
            l=1
            while r-i >= 0 and c+i<=7 : # Diqgonal Top Right:
                if self.board[r-i][c+i][0] =='-':
                    moves.append(Move((r, c), (r-i, c+i), self.board))
                    i+=1
                elif self.board[r-i][c+i][0] =='b':
                    moves.append(Move((r, c), (r-i, c+i), self.board))
                    break
                else:
                    break
            while r-j >=0 and c-j>=0 : # Diagonal Top Left:
                if self.board[r-j][c-j][0 ] =='-':
                    moves.append(Move((r, c), (r-j, c-j), self.board))
                    j+=1
                elif self.board[r-j][c-j][0] =='b':
                    moves.append(Move((r, c), (r-j, c-j), self.board))
                    break
                else:
                    break

            while r+k <=7  and c+k<=7 : # Diagonal Bot Right:
                if self.board[r+k][c+k][0] =='-':
                    moves.append(Move((r, c), (r+k, c+k), self.board))
                    k+=1
                elif self.board[r+k][c+k][0] =='b':
                    moves.append(Move((r, c), (r+k, c+k), self.board))
                    break
                else:
                    break
            while r+l <= 7 and c-l>=0 : # Diagonal Bot Left:
                if self.board[r+l][c-l][0] =='-':
                    moves.append(Move((r, c), (r+l, c-l), self.board))
                    l+=1
                elif self.board[r+l][c-l][0] =='b':
                    moves.append(Move((r, c), (r+l, c-l), self.board))
                    break
                else:
                    break    
        else:
            i=0
            j=0
            k=0
            l=0
            while r-i >= 0 and c+i<=7 : # Diqgonal Top Right:
                if self.board[r-i][c+i][0] =='-':
                    moves.append(Move((r, c), (r-i, c+i), self.board))
                    i+=1
                elif self.board[r-i][c+i][0] =='w':
                    moves.append(Move((r, c), (r-i, c+i), self.board))
                    break
                else:
                    break
            while r-j >=0 and c-j>=0 : # Diagonal Top Left:
                if self.board[r-j][c-j][0 ] =='-':
                    moves.append(Move((r, c), (r-j, c-j), self.board))
                    j+=1
                elif self.board[r-j][c-j][0] =='w':
                    moves.append(Move((r, c), (r-j, c-j), self.board))
                    break
                else:
                    break

            while r+k <=7  and c+k<=7 : # Diagonal Bot Right:
                if self.board[r+k][c+k][0] =='-':
                    moves.append(Move((r, c), (r+k, c+k), self.board))
                    k+=1
                elif self.board[r+k][c+k][0] =='w':
                    moves.append(Move((r, c), (r+k, c+k), self.board))
                    break
                else:
                    break
            while r+l <= 7 and c-l>=0 : # Diagonal Bot Left:
                if self.board[r+l][c-l][0] =='-':
                    moves.append(Move((r, c), (r+l, c-l), self.board))
                    l+=1
                elif self.board[r+l][c-l][0] =='w':
                    moves.append(Move((r, c), (r+l, c-l), self.board))
                    break
                else:
                    break
 """

 #Knight Moves:

""" if  r-2>=0 and c+1<=7:
                if self.board[r-2][c+1][0] =='-' or self.board[r-2][c+1][0] =='b' :   #Top Right
                    moves.append(Move((r, c), (r-2, c+1), self.board))          

            if  r-2>=0 and c-1>=0:
                if self.board[r-2][c-1][0] =='-' or self.board[r-2][c-1][0] =='b':   #Top Left
                    moves.append(Move((r, c), (r-2, c-1), self.board))

            if  r+2<=7 and c+1<=7:
                if self.board[r+2][c+1][0] =='-' or self.board[r+2][c+1][0] =='b':   #Bot Right
                    moves.append(Move((r, c), (r+2, c+1), self.board))

            if  r+2<=7 and c-1>=0:
                if self.board[r+2][c-1][0] =='-' or self.board[r+2][c-1][0] =='b':   #Bot Left
                    moves.append(Move((r, c), (r+2, c-1), self.board))

            if  r-1>=0 and c+2<=7:
                if self.board[r-1][c+2][0] =='-' or self.board[r-1][c+2][0] =='b':   #Right Top
                    moves.append(Move((r, c), (r-1, c+2), self.board))


            if  r+1<=7 and c+2<=7:
                if self.board[r+1][c+2][0] =='-' or self.board[r+1][c+2][0] =='b':   #Right Bot
                    moves.append(Move((r, c), (r+1, c+2), self.board))

            if  r-1>=0 and c-2>=0: 
                if self.board[r-1][c-2][0] =='-' or self.board[r-1][c-2][0] =='b':   #Left top
                    moves.append(Move((r, c), (r-1, c-2), self.board))


            if  r+1<=7  and c-2>=0 :
                if  self.board[r+1][c-2][0] =='-' or self.board[r+1][c-2][0] =='b':   #Left Bot
                    moves.append(Move((r, c), (r+1, c-2), self.board))
        else:
            if  r-2>=0 and c+1<=7:
                if self.board[r-2][c+1][0] =='-' or self.board[r-2][c+1][0] =='w' :   #Top Right
                    moves.append(Move((r, c), (r-2, c+1), self.board))          

            if  r-2>=0 and c-1>=0:
                if self.board[r-2][c-1][0] =='-' or self.board[r-2][c-1][0] =='w':   #Top Left
                    moves.append(Move((r, c), (r-2, c-1), self.board))

            if  r+2<=7 and c+1<=7:
                if self.board[r+2][c+1][0] =='-' or self.board[r+2][c+1][0] =='w':   #Bot Right
                    moves.append(Move((r, c), (r+2, c+1), self.board))

            if  r+2<=7 and c-1>=0:
                if self.board[r+2][c-1][0] =='-' or self.board[r+2][c-1][0] =='w':   #Bot Left
                    moves.append(Move((r, c), (r+2, c-1), self.board))

            if  r-1>=0 and c+2<=7:
                if self.board[r-1][c+2][0] =='-' or self.board[r-1][c+2][0] =='w':   #Right Top
                    moves.append(Move((r, c), (r-1, c+2), self.board))


            if  r+1<=7 and c+2<=7:
                if self.board[r+1][c+2][0] =='-' or self.board[r+1][c+2][0] =='w':   #Right Bot
                    moves.append(Move((r, c), (r+1, c+2), self.board))

            if  r-1>=0 and c-2>=0: 
                if self.board[r-1][c-2][0] =='-' or self.board[r-1][c-2][0] =='w':   #Left top
                    moves.append(Move((r, c), (r-1, c-2), self.board))


            if  r+1<=7  and c-2>=0 :
                if  self.board[r+1][c-2][0] =='-' or self.board[r+1][c-2][0] =='b':   #Left Bot
                    moves.append(Move((r, c), (r+1, c-2), self.board))
"""

#King Moves:
""" 
if self.whiteToMove:
            if c+1<=7 and (self.board[r][c+1][0] =='-' or self.board[r][c+1][0] =='b'):
                moves.append(Move((r, c), (r, c+1), self.board ))        #King Right
            if c-1>=0 and (self.board[r][c-1][0] =='-' or self.board[r][c-1][0] =='b'):
                moves.append(Move((r, c), (r, c-1), self.board ))        #King Left

            if r-1>=0:
                if self.board[r-1][c][0] =='-' or self.board[r-1][c][0] =='b':                      #King Top
                    moves.append(Move((r, c), (r-1, c), self.board ))
                if c+1<=7 and (self.board[r-1][c+1][0] =='-' or self.board[r-1][c+1][0] =='b'):     #King Top Right              
                    moves.append(Move((r, c), (r-1, c+1), self.board ))
                if c-1>=0 and (self.board[r-1][c-1][0] =='-' or self.board[r-1][c-1][0] =='b'):     #King Top Left
                    moves.append(Move((r, c), (r-1, c-1), self.board ))
            if r+1<=7:
                if self.board[r+1][c][0] =='-' or self.board[r+1][c][0] =='b':                      #King back
                    moves.append(Move((r, c), (r+1, c), self.board ))
                if c+1<=7 and (self.board[r+1][c+1][0] =='-' or self.board[r-1][c+1][0] =='b'):     #King Bot Right         
                    moves.append(Move((r, c), (r+1, c+1), self.board ))
                if c-1>=0 and (self.board[r+1][c-1][0] =='-' or self.board[r-1][c-1][0] =='b'):     #King Bot Left
                    moves.append(Move((r, c), (r+1, c-1), self.board ))
        else:  #Blck to Move
            if c+1<=7 and (self.board[r][c+1][0] =='-' or self.board[r][c+1][0] =='w'):
                moves.append(Move((r, c), (r, c+1), self.board ))        #King Right
            if c-1>=0 and (self.board[r][c-1][0] =='-' or self.board[r][c-1][0] =='w'):
                moves.append(Move((r, c), (r, c-1), self.board ))        #King Left

            if r-1>=0:
                if self.board[r-1][c][0] =='-' or self.board[r-1][c][0] =='w':                      #King Top
                    moves.append(Move((r, c), (r-1, c), self.board ))
                if c+1<=7 and (self.board[r-1][c+1][0] =='-' or self.board[r-1][c+1][0] =='w'):     #King Top Right              
                    moves.append(Move((r, c), (r-1, c+1), self.board ))
                if c-1>=0 and (self.board[r-1][c-1][0] =='-' or self.board[r-1][c-1][0] =='w'):     #King Top Left
                    moves.append(Move((r, c), (r-1, c-1), self.board ))
            if r+1<=7:
                if self.board[r+1][c][0] =='-' or self.board[r+1][c][0] =='w':                      #King back
                    moves.append(Move((r, c), (r+1, c), self.board ))
                if c+1<=7 and (self.board[r+1][c+1][0] =='-' or self.board[r-1][c+1][0] =='w'):     #King Bot Right         
                    moves.append(Move((r, c), (r+1, c+1), self.board ))
                if c-1>=0 and (self.board[r+1][c-1][0] =='-' or self.board[r-1][c-1][0] =='w'):     #King Bot Left
                    moves.append(Move((r, c), (r+1, c-1), self.board )) """
            