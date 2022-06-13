class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx= pointer = nums[0]
        
        
        
        for i in range(1,len(nums)):
            if pointer < 0:
                pointer = 0
            pointer += nums[i]
            if pointer > maxx:
                maxx = pointer
            
               
            
            
        return(maxx)
    
        
            
        
        
        