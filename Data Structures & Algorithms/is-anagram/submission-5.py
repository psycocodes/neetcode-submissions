class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if (n != m): return False
        charset = {}
        for char in s:
            if char not in charset:
                charset[char] = 1
            else:
                charset[char] +=1

        for char in t:
            if char not in charset:
                print(f"{char} not in charset, returning false")
                return False
            else:
                d = charset[char] - 1
                if d==0:
                    del charset[char]
                else:
                    charset[char] -= 1
        return not bool(charset)