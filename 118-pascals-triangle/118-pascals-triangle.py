class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        if(numRows>=2):
            result.append([1,1])
        
        for i in range(2,numRows):
            l=[]
            l.append(1)
            for j in range(len(result[i-1])-1):
                l.append(result[i-1][j]+result[i-1][j+1])
                
                
            l.append(1)
            result.append(l)
            
            
        return result
                
            
        
        