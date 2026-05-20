class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            while (l <= len(s)-1) and ((not s[l].isalnum()) or s[l] == " "):
                l+=1
            while (r >= 0) and ((not s[r].isalnum()) or s[r] == " ") and r >= 0:
                r-=1
            if l > r: break
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
                continue
            else:
                return False
        return True