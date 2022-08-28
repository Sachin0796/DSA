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
            
        oldColor = image[sr][sc]
        n = len(image)
        m = len(image[0])        
        if oldColor == color:
            return image
        a = flood(image, sr, sc, oldColor, color, n, m)        
        return a