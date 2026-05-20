class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    triplet = (nums[i], complement, nums[j])
                    res.add(triplet)
                seen.add(nums[j])
        return [list(_) for _ in res]
