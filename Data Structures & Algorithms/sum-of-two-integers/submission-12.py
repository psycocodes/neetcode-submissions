class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            _a = (a >> i) & 1
            _b = (b >> i) & 1
            s, carry = Solution.fullAdder(_a, _b, carry)
            res |= s << i
        res = res | carry << 32
        res = res & 0xFFFFFFFF 
        print(bin(res))
        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF) 
        print(bin(res))
        return res
        
        
            

    @staticmethod
    def halfAdder(x, y):
        return x^y, x&y
    @staticmethod
    def fullAdder(x, y, ci):
        _s1, _c1 = Solution.halfAdder(x, y)
        s, _c2 = Solution.halfAdder(_s1, ci)
        c = _c1 | _c2
        return s, c

