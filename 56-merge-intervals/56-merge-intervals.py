class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals)
        intervals.sort()
        temp = intervals[0]
        result = []
        for i in range(l):
            temp1 = temp[0]
            temp2 = temp[1]
            temp3 = intervals[i][0]
            temp4 = intervals[i][1]    
            x = set([i for i in range(temp1,temp2+1)]) & set([j for j in range(temp3,temp4+1)])
            
            if len(x)!=0:
                temp[0]= temp1 if temp1<=temp3 else temp3
                temp[1]= temp2 if temp2>=temp4 else temp4
                if i==l-1:
                    result.append(temp)
            else:
                result.append(temp)
                temp = intervals[i]
                if i==l-1:
                    result.append(temp)
        return result
                    