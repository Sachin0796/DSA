def searchMaze(arr, n):
        
    ans= []
    def findPaths(arr, i, j, n, m, tempAns, ans):
        if i == n-1 and j == m-1 and arr[i][j] == 1:
            ans.append(tempAns)
            return
        if i == n or j == m or arr[i][j] != 1:
            return
        findPaths(arr, i+1, j, n, m, tempAns+'D', ans)
        findPaths(arr, i-1, j, n, m, tempAns+'U', ans)
        findPaths(arr, i, j+1, n, m, tempAns+'R', ans)
        findPaths(arr, i, j-1, n, m, tempAns+'L', ans)
    
    findPaths(arr, 0, 0, n, n, '', ans)
    return ans


searchMaze([[1,0],[1,1]], 2)