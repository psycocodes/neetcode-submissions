class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            res = 0
            for j in range(10):
                res += (i & 1) 
                i = i >> 1
            l.append(res)
        return l
            