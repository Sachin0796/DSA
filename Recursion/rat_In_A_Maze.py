# Runnable code in coding ninja
# Link - https://www.codingninjas.com/codestudio/problems/rat-in-a-maze_1215030?source=youtube&campaign=Recursion_Fraz&utm_source=youtube&utm_medium=affiliate&utm_campaign=Recursion_Fraz&leftPanelTab=1

def searchMaze(arr, n):
        
    ans= []
    def findPaths(arr, i, j, n, m, tempAns, ans):
        
        if i == n-1 and j == m-1 and arr[i][j] == 1:
            ans.append(tempAns)
            return
        
        elif i < 0 or j < 0 or i == n or j == m or arr[i][j] != 1:
            return        
        
        ch = arr[i][j]
        arr[i][j] = '#'
        
        findPaths(arr, i+1, j, n, m, tempAns+'D', ans)
        findPaths(arr, i-1, j, n, m, tempAns+'U', ans)
        findPaths(arr, i, j+1, n, m, tempAns+'R', ans)
        findPaths(arr, i, j-1, n, m, tempAns+'L', ans)
    
        arr[i][j] = ch
        return 
    
    findPaths(arr, 0, 0, n, n, '', ans)
    ans.sort() # I was missing this
    return ans

    