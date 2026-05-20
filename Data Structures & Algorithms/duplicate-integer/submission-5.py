class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for e in nums:
            if e in h:
                return True
            else:
                h.add(e)
        return False
        