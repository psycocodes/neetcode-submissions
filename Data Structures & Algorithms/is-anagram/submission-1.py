class Solution:
    def Counter(self, string: str)->dict:
        return {character: string.count(character) for character in string}

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
                