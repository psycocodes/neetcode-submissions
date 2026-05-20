class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        max_count = 0
        count = 0
        start = 0
        for i in range(len(nums)):
            current = nums[i]
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1

            max_count = max(length, max_count)
        return max_count
            
                
                
                
                
            