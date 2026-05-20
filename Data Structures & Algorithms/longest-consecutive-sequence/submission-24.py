class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for number in nums: 
            if (number-1) not in numset:
                length = 1
                while (number+length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest
            
