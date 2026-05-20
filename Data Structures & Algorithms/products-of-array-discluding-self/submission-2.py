class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, N = nums, len(nums)
        p=[1]*N
        s=[1]*N
        for i in range(1,N):
            p[i] = n[i-1]*p[i-1]
            s[N-i-1] = n[N-i]*s[N-i]
        return [p*s for p,s in zip(p,s)]