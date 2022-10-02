class maxLengthConcat:
    maxL = 0
    
    @classmethod
    def changemaxValue(cls, newL):
        if cls.maxL<newL:            
            cls.maxL = newL
            return

    def maxLengthConcatination(self, arr, tempAns, index):        
        
        if index == len(arr):                             
            if len(set(tempAns)) == len(tempAns):
                self.changemaxValue(len(tempAns))              
            return 
            
        #take
        self.maxLengthConcatination(arr, tempAns+arr[index], index+1)        
        #not take
        self.maxLengthConcatination(arr, tempAns, index+1)
    
a = ['cha','r','act','ers']
c = maxLengthConcat()
c.maxLengthConcatination(a, '', 0)
print(c.maxL)