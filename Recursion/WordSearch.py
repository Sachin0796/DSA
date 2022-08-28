#Runnable code in leetcode
# Problem link - https://leetcode.com/problems/word-search/submissions/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def findWord(board, word, x, y, n, m, tempAns, k):
            
            if tempAns ==  word:
                return True
            
            if k < len(word):
                if x < 0 or y < 0 or x == n or y == m or board[x][y] != word[k]:
                    return False   
            else:
                return True
            
            ch = board[x][y]            
            board[x][y] = '#'
            
            a = findWord(board, word, x+1, y, n, m, tempAns + board[x][y], k+1)
            b = findWord(board, word, x-1, y, n, m, tempAns + board[x][y], k+1)
            c = findWord(board, word, x, y+1, n, m, tempAns + board[x][y], k+1)
            d = findWord(board, word, x, y-1, n, m, tempAns + board[x][y], k+1)
            
            board[x][y] = ch
            
            return a or b or c or d
        x = -1
        y = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    x = i
                    y = j
                    if findWord(board, word, x, y, len(board), len(board[0]), '', 0):
                        return True
                    
            x = -1
            y = -1            
        return False