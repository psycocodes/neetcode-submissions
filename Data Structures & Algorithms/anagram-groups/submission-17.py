class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs: 
            count = [0]*26
            for char in string: 
                count[ord(char)-97] += 1
            res[tuple(count)].append(string)
        print(res.values())
        return list(res.values())