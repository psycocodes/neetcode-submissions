class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = list(range(len(nums)+1))
        for num in L:
            if num in sorted(nums):
                 continue
            return num
            