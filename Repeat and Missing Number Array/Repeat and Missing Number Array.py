class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        result = []
        l = [0] * len(A)
        l.append(0)
        for i in A:
            l[i] +=1
            
        result.append(l.index(2))
        l.pop(0)
        result.append(l.index(0)+1)
        
        return result