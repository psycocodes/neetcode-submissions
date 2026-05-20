class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        w = 0
        for i in range(32):
   	        w += ((n & (mask << i)) >> i) & 1
        return w