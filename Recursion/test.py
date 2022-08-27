nums=[1,2,3,1]
visited = [False] * len(nums)
def robSum(nums, index, tempSum):
    if index >= len(nums):
        return tempSum
    
    if visited[index] == True:
        robSum(nums, index+2, tempSum + nums[index])
    else:
        visited[index] = True
        a = robSum(nums, index+2, tempSum + nums[index])
        
        visited[index] = False
        b = robSum(nums, index+1, tempSum)
        
        return max(a, b)

print(robSum(nums, 0, 0))