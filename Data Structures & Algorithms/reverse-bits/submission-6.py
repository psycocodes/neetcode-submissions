class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        m = 32 #Constant Time
        for i in range(m):
            shifted_binary = ((n>>i)&1) << (m-1-i)
            print(f"{bin(n)}: [{m-1-i}]{bin((n>>i)&1)}: {shifted_binary} ")
            output += shifted_binary
        print(bin(output))
        return output 