# Working Leetcode code:

# Problem link: https://leetcode.com/problems/n-queens/

# Approach to the problem and some assumptions:

# We are going row by row, and we are making sure that each row will have a queen in it otherwise we will not move to the next row. So considering this, we can start the row value with 0 i.e. i and we can loop through our columns using j and place the queen in all the columns using i,j in chessBoard untill we see that row count i.e. i(starting 0)  == n


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        chessBoard = [["." for i in range(n)] for j in range(n)]       
        
        def validPath(chessBoard, i, j, n):                   
            
            #UP
            tempI = i
            while tempI >= 0:
                if chessBoard[tempI][j] == "Q":
                    return False                    
                tempI-=1
                    
            #TOP RIGHT
            tempI = i
            tempJ = j
            while tempI >= 0 and tempJ <= n-1:
                if chessBoard[tempI][tempJ] == "Q":
                    return False                    
                tempI-=1
                tempJ+=1
                 
            #TOP LEFT
            tempI = i
            tempJ = j
            while tempI >= 0 and tempJ >= 0:
                if chessBoard[tempI][tempJ] == "Q":
                    return False                    
                tempI-=1
                tempJ-=1            
            return True
        
        def possibleWays(chessBoard, n, i, ans):
            if i == n:                  
                ans.append([''.join(row) for row in chessBoard])                
                return
            
            for j in range(n):                   
                if validPath(chessBoard, i, j, n):                       
                    chessBoard[i][j] = "Q"                    
                    possibleWays(chessBoard, n, i+1, ans)                    
                    chessBoard[i][j] = "."
        
        possibleWays(chessBoard, n, 0, ans)
        return ans