class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
        