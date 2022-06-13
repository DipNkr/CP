class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        one_count = nums.count(1)
        two_count = nums.count(2)
        
        for i in range(zero_count):
            nums[i]=0
            
        for i in range(zero_count,zero_count+one_count):
            nums[i]=1
            
        for i in range(zero_count+one_count,zero_count+one_count+two_count):
            nums[i]=2