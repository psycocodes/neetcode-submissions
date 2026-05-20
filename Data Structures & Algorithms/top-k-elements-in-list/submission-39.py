class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) space means one list of n elements
        # O(n) time means atmost one for loop
        # We will be using bucket sort, that groups elements based on their frequency
        numberset = set(nums)
        n = len(numberset)
        buckets = [[] for _ in range(n)]
        for number in set(nums):
            buckets[n - nums.count(number)].append(number)
        return [number for bucket in buckets for number in bucket][:k]