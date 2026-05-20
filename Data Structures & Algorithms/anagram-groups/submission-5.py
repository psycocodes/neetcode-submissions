class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = ["".join(sorted(x)) for x in strs]
        unique_strings = list(set(sorted_strings))
        sorted_strings = list(map(lambda string: unique_strings.index(string), sorted_strings))
        output = [[] for _ in range(len(unique_strings))]
        o = []
        print(sorted_strings)
        print(output)
        print(unique_strings)
        for i in range(len(sorted_strings)):
            print(f"{i=} : {sorted_strings[i]=} : {strs[i]=}")
            output[sorted_strings[i]].append(strs[i])
        return output
