class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remembered = {}

        for i in range(len(nums)): 
            if nums[i] in remembered: 
                return True
            remembered[nums[i]] = 1
    
        return False