class ChessBoard():    
    def __init__(self, n, m) :    
        self.Chess = [["*" for i in range(n)] for i in range(m)]
        # print(self.Chess)        
    

    def putPiece(self, x, y, piece):
        
        if x>7 or x<0 or y>7 or y<0:
            print("Not a valid path")
            return
            
        if self.Chess[x][y] != "*":
            print("Square occupied!")
            return
        
        self.Chess[x][y] = piece
        return

    def isValidDiagonal(self, sr, sc, er, ec, n):        
        #left upwards        
        temp_sr = sr
        temp_sc = sc
        while temp_sr >=0  and temp_sc < n:
            if temp_sr == er and temp_sc == ec:
                return True
            temp_sr -= 1
            temp_sc += 1        

        #left downwards
        temp_sr = sr
        temp_sc = sc        
        while temp_sr < n and temp_sc < n:
            if temp_sr == er and temp_sc == ec:
                return True
            temp_sr += 1
            temp_sc += 1        

        #right upwards
        temp_sr = sr
        temp_sc = sc
        while temp_sr >= 0 and temp_sc >= 0:
            if temp_sr == er and temp_sc == ec:
                return True
            temp_sr -= 1
            temp_sc -= 1        

        #right downwards
        temp_sr = sr
        temp_sc = sc
        while temp_sr >= 0 and temp_sc >= 0:
            if temp_sr == er and temp_sc == ec:
                return True
            temp_sr += 1
            temp_sc -= 1        

        return False

cb = ChessBoard(8, 8)
cb.putPiece(0, 0, 'H')
print(cb.Chess)
a = cb.isValidDiagonal(0, 0, 6, 6, 8)
print(a)