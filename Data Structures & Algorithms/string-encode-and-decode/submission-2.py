class Solution:
    
    def encode(self, strs: List[str]) -> str:
        delimiter = "%"
        return delimiter + "".join([f"{len(string)}{delimiter}{string}" for string in strs])

    def decode(self, s: str) -> List[str]:
        delimiter, s = s[0], s[1:]
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            strs.append(s[word_start:word_end])
            i = word_end

        return strs
