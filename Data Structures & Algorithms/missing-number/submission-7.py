class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = list(range(len(nums)+1))
        nums = sorted(nums)
        for num in L:
            if num not in nums:
                return num
            