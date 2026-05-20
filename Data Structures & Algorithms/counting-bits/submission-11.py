class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        k=0
        for i in range(1,n+1):
            print(f"i:{i}, k: {k}, 2**k: {2**k}, i-2**k: {i-2**k}")
            output[i] = output[i-2**k] + 1
            if i-2**k == 2**k-1: k+=1
        return output