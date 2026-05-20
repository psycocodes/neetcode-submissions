class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = list(range(len(nums)+1))
        for num in L:
            if num not in sorted(nums):
                return num
            