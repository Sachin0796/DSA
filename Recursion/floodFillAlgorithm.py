
# This is a runnable code in leetcode. Same can be used in coding ninja. Sample input can be taken from platform. Below is the link for the code:

# Leetcode - https://leetcode.com/problems/flood-fill/submissions/
# Coding Ninja -  https://www.codingninjas.com/codestudio/problems/flood-fill-algorithm_1089687?leftPanelTab=1

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def flood(image, x, y, oldColor, newColor, n, m):            
            if x < 0 or  y < 0 or x == n or y == m or image[x][y] != oldColor:
                return
            image[x][y] = newColor
            flood(image, x+1, y, oldColor, newColor, n, m)
            flood(image, x-1, y, oldColor, newColor, n, m)
            flood(image, x, y+1, oldColor, newColor, n, m)
            flood(image, x, y-1, oldColor, newColor, n, m)
                        
            return image
        # Here in this code, backtracking is not required because we are filling the cell with new color and adding the check in base condition that if given cell color is not old color, then just simply return and since we are adding the newColor if we are moving to the cell, then we dont need the backtracking of any kind or to change the given cell with any other value.    
        oldColor = image[sr][sc]
        n = len(image)
        m = len(image[0])        
        if oldColor == color:
            return image
        a = flood(image, sr, sc, oldColor, color, n, m)        
        return a