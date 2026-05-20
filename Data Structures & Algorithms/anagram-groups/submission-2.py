class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = [string]
            else:
                res[tuple(count)].append(string)
        return list(res.values())