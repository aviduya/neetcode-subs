class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cleaned = set(nums)
        output = 0

        for num in cleaned: 
            curr = num
            if num - 1 not in cleaned:
                streak = 0
                while curr in cleaned: 
                    streak += 1
                    curr += 1
                output = max(output, streak)

            
        return output
